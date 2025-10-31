import time
from collections import Counter
maksimiPisteet = 6
CGREEN  = '\33[32m'
CVIOLET = '\33[35m'
CEND      = '\33[0m'

# eph:den kahta viimeistä avainta ei näytetä pelaajalle, ne sisältävät aina
# pelin sisäistä dataa
epht = {
    'isäntä': {
        'tehtävä' : 'Tuo minulle kirjani. Se jäi kellariin.',
        'avain' : 'Tarvitset tämän avaimen että saat oven auki.',
        'lamppu' : 'Ota lamppu niin se grue ei syö sinua!',
        'grue' : 'Kellarissa asustaa kamala grue!',
        'kellari' : 'Se on tuossa alakerrassa.',
        'kirja' : 'Se on minulle kallisarvoinen.',
        'haluaa' : 'kirja',
        'esineet' : ['myyrä']
    },
    'grue' : {
        'grue' : 'Olen grue. Popsin sinut suihini!!!',
        'tehtävä' : 'Anna minulle tuo lamppu. Kaipaan sitä niin.',
        'kirja' : 'Siinä lukee NECRONIMICON kannessa, vaikuttaa epäilyttävältä.',
        'haluaa' : 'lamppu',
        'esineet' : []
    }
}


paikat = [
        {'tupa' :'tupa',
        'tarina': 'Olet vanhassa hollituvassa.',
        'esineet': {'avain': 'avain', 'lamppu': 'lamppu'},
        'hahmot': 'isäntä',
        'puhe' : 'Tervehdys matkalainen! Olisi vähän asiaa.',
        'ovi' : {'auki': False, 'suunta' : 'kellari', 'avaa' : 'avain' },
        },
        {'kellari': 'kellari',
         'tarina': 'Onpa täällä pimeää. Hui! Siut todennäköisesti syö grue.',
         'esineet': {'kirja': 'kirja'},
         'hahmot' : 'grue',
         'puhe' : 'Maiskis!',
         'ovi' : {'auki': True, 'suunta' : 'tupa' },
        }
]

## näistä voi kysyä lisätietoja
esineet = {
    'lamppu' : {
        'kuvaus': 'Kiva lamppu. Nytpä saa grue pitkän nenän.',
        'synonyymi': 'kivasti valaiseva lamppu'
    },
    'avain' : {
        'kuvaus': 'Vanha ruosteinen avain. Avaa kellarin oven.',
        'synonyymi' : 'kellarin avain'
    },
    'kirja' : {
        'kuvaus': 'Pahaenteinen nahkakantinen kirja. Kirjoittanut Abdul Alhazred.',
        'synonyymi' : 'necronomicon'
    },
    'isäntä' :
        {'kuvaus' : 'Epämääräisen oloinen kaveri. Jostain syystä niskakarvasi nousevat pystyyn kun puhut hänen kanssaan.' }
}


tupa = paikat[0]
kellari = paikat[1]

## komentolistaus, itse asiassa komennot poistetaan, mutta 'tekokelpoiset'
## listat voi säilyttää
coms = [
    {'ota':'ota',
     'otettavat' : [*esineet.keys()]
    },
    {
    'avaa': 'avaa',
    'avattavat': ['ovi', 'reppu']
    },
    {'kuvaile': 'kuvaile',
    'kuvailtavat': ['paikka', *esineet.keys()]
    },
    {'mene': 'mene',
     'mentavat': ['tupaan', 'kellariin']},
    {'kysy' : 'kysy',
     },
    {'anna' : 'anna'}
]

# pisteet arvot muutetaan 1, jos pistetavoite saavutetaan
## mietitään vielä saako true tai false iteroitua, mutta
# counter iteroi lukuarvot erittäin helposti
pisteet = {
    'lamppuOtettu' : 0,
    'kirjaAnnettu' : 0,
    'kirjaLuettu' : 0
}


# selvitellään tarvitseeko näitä ollenkaan

ottaa = coms[0]
avata = coms[1]
kuvaile = coms[2]
menna = coms[3]
kysy = coms[4]
anna = coms[5]

# pelaajaobjekti

pelaaja = {'pisteet': 0,
           'paikka' : '',
           'paikkaIndeksi': 0,
           'reppu': []}

# palauttaa paikkaindeksin eri paikoille

def checkIndex(place):
    if place == 'tupa':
        return 0
    elif place == 'kellari':
        return 1

# luo listan asioista joita eph:lta voi kysyä
def rakennaKysyttavat():
    indeksi = checkIndex(pelaaja['paikka'])
    return [*epht[paikat[indeksi]['hahmot']].keys()]

# tarkistaa onko annettu tavara repussa
def tarkistaOnkoRepussa(esine):
    if esine in pelaaja['reppu']:
        return True
    else:
        printText(f'{esine.upper()} ei ole repussasi.')
        print()
        return False

# Kirjoittaa alkutarinan näytlölle. todennäköisesti hoidetaan muuten lopullisessa versiossa
def showStart():
    print("Majatalon isäntä on huhuillut sinut sisään. Hän vaikuttaa hermostuneelta.")
    print()

# kirjoittaa näytölle paikka-objekti tarina-avaimen arvon.
def showStory():
    print(f"{paikat[pelaaja['paikkaIndeksi']]['tarina']}")
    print()

# kertoo kuvauksen pelaajan paikasta pelimaailmassa. Voidaan jaotella osiin?
def checkWhere(indeksi):
    printText(f"Olet paikassa {pelaaja['paikka'].upper()}.")

    if paikat[indeksi]['ovi']:
        printText(f'Täällä on ovi, se johtaa paikkaan {paikat[indeksi]['ovi']['suunta']}.')

    if paikat[indeksi]['ovi']['auki']:

        printText(f'Ovi on auki')
    elif paikat[indeksi]['ovi']['auki'] == False:
        printText('Ovi on lukossa.')

    printText(f'Täällä on {paikat[indeksi]['hahmot']}.')
    printText(f'Hän sanoo "{paikat[indeksi]['puhe']}"')
    print()
    printText('Voit kysyä häneltä seuraavia asioita:' )

    asiat = list(epht[paikat[indeksi]['hahmot']])
    asiatPituus = len(asiat) -2
    asiatRivissa =''
    for i in range(asiatPituus):
        asiatRivissa += CGREEN + asiat[i] + CEND + ' '
    printText(asiatRivissa)
    print()

    esineetRivissa =''
    if len(paikat[indeksi]['esineet'])> 0:
        printText(f'{CVIOLET}Täältä löytyy: {CEND}')
        for esine in paikat[indeksi]['esineet']:
            esineetRivissa += CVIOLET + esine + CEND + ' '

        printText(esineetRivissa)
        print()
    else:
        printText("Huoneessa ei ole poimittavia esineitä.")

# tarkistaa onko kysytty esine huoneessa, jossei, sen kuvausta ei näytetä
def checkIfItemInRoom(item):
    if item in paikat[pelaaja['paikkaIndeksi']]['esineet']:
        return True
    elif item in epht:
        return True
    else:
        return False

# tulostaa kuvauksen esineestä. Voidaan yhdistää edelliseen chekIfItemInRoom -funktioon
def checkItem(item):
    if item == 'kirja':
        pisteet['kirjaLuettu'] = 1
    print(f'{esineet[item]['kuvaus']}')

# asettaa pelaajan paikka ja paikkaindeksi -arvot
def setPlayerPlace(place, index):
    pelaaja['paikka'] = place
    pelaaja['paikkaIndeksi'] = index

# lisää esineen pelaajan tavaroihin ja poistaa sen oaikan tavaroista
def addToIventory(item, placeIndex):
    if item in paikat[placeIndex]['esineet'].keys():
        pelaaja['reppu'].append(item)
        paikat[placeIndex]['esineet'].pop(item)
        printText(f'{esineet[item]['synonyymi'].upper()} lisätty reppuun!')
        print()
    else:
        printText(f'Esinettä {item} ei löydy täältä.')

# antaa pelaajan tavaran eph:lle. pitää nimetä uudelleen
def removeFromInventory(item):
    epht[paikat[pelaaja['paikkaIndeksi']]['hahmot']]['esineet'].append(item)
    pelaaja['reppu'].remove(item)

# näyttää pelaajan tavarat
def showInventory():
    if len(pelaaja['reppu']) > 0:
        printText("Repussasi on:")
        for item in pelaaja['reppu']:
            printText(CGREEN + esineet[item]['synonyymi'].upper() + CEND)
    else:
        printText('Reppusi on tyhjä.')
    print()

# kertoo tarkemman kuvauksen esineestä
def tellMeMore(question, index):
    hahmo = paikat[index]['hahmot']
    print(f'{hahmo.capitalize()} sanoo "{epht[hahmo][question]}"')

# tarkistaa täyttyykö pelaajan kuolinehto, tai sen pelastusehto
def checkForDeath(place, index):
    if place == 'kellari' and 'lamppu' not in pelaaja['reppu']:
        printText(f'Sinut söi kamala {paikat[index]['hahmot']}!')
        printText(f'{paikat[index]['puhe']}')
        return True
    elif place == 'kellari' and 'lamppu' in pelaaja['reppu']:
        printText(f'Lamppu pelasti sinut kamalan {paikat[index]['hahmot']}n kynsistä. HUH! ')
        return False

# tarkistaa ottaako eph vastaan tarjotun esineen
def tarkistaHaluaako(esine, haluttuEsine):
    if esine == haluttuEsine:
        return True
    else:
        return False

# pistetarkistuksia, UUSIKSI vilä asioita tässä mutta toimii
def tarkistaPisteet():
    if 'kirja' in epht['isäntä']['esineet']:
        pisteet['kirjaAnnettu'] = 1
    if 'lamppu' in pelaaja['reppu']:
        pisteet['lamppuOtettu'] = 1

# tarkistaa voitttoehdon toteutumisen, tätä voi vielä kehittää
# koska avainsanat täällä
def tarkistaVoitto():
    if 'kirja' in epht['isäntä']['esineet']:
        return True
    else:
        return False
# jos pelaaja toimii erittäin tyhmästi, tämä laukeaa
def tarkistaTyhmyys():
    if 'lamppu' in epht['grue']['esineet']:
        return True
    else:
        return False

# jos tullee tuntematon komento, tämä ajetaan
def unableToExecute():
    printText('Anteeksi, en ymmärtänyt.')
    print()

# kustomoitu print() funktio
def printText(string):
    for char in string:
        print(char, end='', flush=True)
        time.sleep(.05)
    print()

# sallii suomen kieliopin mukaiset suunnat
def convertToBasicForm(place):
    if place == 'tupaan':
        return 'tupa'
    elif place == 'kellariin':
        return 'kellari'
    else:
        return place

#pistelaskuri
def countPoints():
    multiplier = Counter(list([*pisteet.values()]))
    return multiplier[1] * 2


showStart()
showStory()
setPlayerPlace(tupa['tupa'], 0)
komento = input('Mitä teet?> ').strip().lower()


while komento != ('lopeta'):
    sanaMaara = 0
    for item in komento.split(" "):
        sanaMaara = sanaMaara + 1

    komentoLista = komento.split(" ")

    if sanaMaara == 1 and komento == 'apua':
            printText('Apua saa täältä!')
            aputiedosto = open("demohelp.txt")
            print(aputiedosto.read())
            print()

    elif sanaMaara == 1 and komento == 'mukana':
        showInventory()

    elif sanaMaara == 1:
        unableToExecute()
    elif sanaMaara == 2:
        verbi = komentoLista[0]
        substantiivi = komentoLista[1]

        try:
            if (verbi == ottaa['ota']) and substantiivi in ottaa['otettavat']:
                paikkaIndeksi = pelaaja['paikkaIndeksi']
                addToIventory(substantiivi, paikkaIndeksi)


            elif(verbi == 'kuvaile'):
                if substantiivi == pelaaja['paikka'] or substantiivi == 'paikka':
                    paikkaIndeksi = pelaaja['paikkaIndeksi']
                    checkWhere(paikkaIndeksi)
                else:
                    if(checkIfItemInRoom(substantiivi)):
                        checkItem(substantiivi)
                    else:
                        print('Esinettä ei ole täällä.')

            elif((verbi == menna['mene'] and substantiivi in menna['mentavat']) or (verbi == 'avaa' and substantiivi == 'ovi')):
                if verbi == 'avaa':
                    verbi = 'mene'
                    paikkaIndeksi = pelaaja['paikkaIndeksi']
                    substantiivi = paikat[paikkaIndeksi]['ovi']['suunta']



                vanhaPaikka = pelaaja['paikka']
                vanhaPaikkaIndeksi = checkIndex(vanhaPaikka)
                uusiPaikka = convertToBasicForm(substantiivi)
                paikkaIndeksi = checkIndex(uusiPaikka)


                if paikat[vanhaPaikkaIndeksi]['ovi']['auki']:
                    setPlayerPlace(uusiPaikka, paikkaIndeksi)
                    printText(paikat[paikkaIndeksi][uusiPaikka].upper())
                    printText(paikat[paikkaIndeksi]['tarina'])

                elif paikat[vanhaPaikkaIndeksi]['ovi']['auki'] == False:

                    if paikat[vanhaPaikkaIndeksi]['ovi']['avaa'] in pelaaja['reppu']:
                        printText('Avaat oven ja astut urheasti eteenpäin.')
                        uusiPaikka = convertToBasicForm(substantiivi)
                        paikkaIndeksi = checkIndex(uusiPaikka)
                        setPlayerPlace(uusiPaikka, paikkaIndeksi)
                        printText(paikat[paikkaIndeksi][uusiPaikka].upper())
                        printText(paikat[paikkaIndeksi]['tarina'])
                        substantiivi = uusiPaikka

                    else:
                        print(f'Oveen tarvitaan {paikat[vanhaPaikkaIndeksi]['ovi']['avaa']}.')
                        paikkaIndeksi = checkIndex(vanhaPaikka)
                        setPlayerPlace(vanhaPaikka, paikkaIndeksi)
                        substantiivi = vanhaPaikka



                paikkaIndeksi = checkIndex(substantiivi)

                if (checkForDeath(substantiivi, paikkaIndeksi)):
                    printText('Voi sentään. Kuolit. Peli päättyi.')
                    break


            elif(verbi == 'kysy' and substantiivi in rakennaKysyttavat()):
                paikkaIndeksi = checkIndex(pelaaja['paikka'])
                tellMeMore(substantiivi, paikkaIndeksi)

            elif(verbi == 'anna'):
                if tarkistaOnkoRepussa(substantiivi):
                    if tarkistaHaluaako(substantiivi, epht[paikat[pelaaja['paikkaIndeksi']]['hahmot']]['haluaa']):
                        print(f'{paikat[pelaaja['paikkaIndeksi']]['hahmot'].capitalize()} ottaa esineen {substantiivi} ja sujauttaa sen talteen.')
                        removeFromInventory(substantiivi)

                    else:
                        print(f'{paikat[pelaaja['paikkaIndeksi']]['hahmot'].capitalize()} toteaa "{substantiivi.capitalize()} ei kelpaa minulle!"')

            else:
                unableToExecute()
        except:
            print(f'kaatuu: "{verbi}" tai "{substantiivi}" ei ole tuettujen komentojen joukossa. Kirjoita "apua" nähdäksesi sallitut komennot.')
    else:
        unableToExecute()
    tarkistaPisteet()
    pelaaja["pisteet"] = countPoints()

    if(tarkistaTyhmyys()):
        print('Ei voi olla totta!')
        print('Miksi teit noin. Nyt grue syö sinut!')
        break

    if(tarkistaVoitto()):
        print('Huikeaa, isäntä sai kirjansa ja pääsee noitumaan!')
        print('Olet voittanut!')
        break


    print(f'Pisteet: {pelaaja["pisteet"]}/{maksimiPisteet}')
    komento = input('Mitä teet?> ').strip().lower()


printText(f'Ensi kertaan! Lopulliset pisteesi ovat: {pelaaja["pisteet"]}/{maksimiPisteet}.')


