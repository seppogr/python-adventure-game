import time
maksimiPisteet = 20
CGREEN  = '\33[32m'
CEND      = '\33[0m'

epht = {
    'isäntä': {
        'tehtävä' : 'Tuo minulle kirjani. Se jäi kellariin.',
        'avain' : 'Tarvitset tämän avaimen että saat oven auki.',
        'lamppu' : 'Ota lamppu niin se grue ei syö sinua!',
        'grue' : 'Kellarissa asustaa kamala grue!',
        'kellari' : 'Se on tuossa alakerrassa.',
        'haluaa' : 'kirja',
        'esineet' : ['myyrä']
    },
    'grue' : {
        'mikä' : 'Olen grue. Popsin sinut suihini!!!',
        'tehtävä' : 'Anna minulle tuo lamppu. Kaipaan sitä niin.',
        'haluaa' : 'lamppu',
        'esineet' : []
    }
}

paikat = [
        {'tupa' :'tupa',
        'tarina': 'Olet vanhassa hollituvassa.',
        'esineet': {'avain': 'avain', 'lamppu': 'lamppu'},
        'hahmot': 'isäntä',
        'puhe' : 'Tervehdys matkalainen!',
        'tiedustelut' : [*epht['isäntä'].keys()]
        },
        {'kellari': 'kellari',
         'tarina': 'Onpa täällä pimeää. Hui! Siut todennäköisesti syö grue.',
         'esineet': {'kirja': 'kirja'},
         'hahmot' : 'grue',
         'puhe' : 'Maiskis!'
        }
]

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
    }
}


tupa = paikat[0]
kellari = paikat[1]

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




ottaa = coms[0]
avata = coms[1]
kuvaile = coms[2]
menna = coms[3]
kysy = coms[4]



pelaaja = {'pisteet': 0,
           'paikka' : '',
           'paikkaIndeksi': 0,
           'reppu': []}

def checkIndex(place):
    if place == 'tupa':
        return 0
    elif place == 'kellari':
        return 1

def rakennaKysyttavat():
    indeksi = checkIndex(pelaaja['paikka'])
    return [*epht[paikat[indeksi]['hahmot']].keys()]

def tarkistaOnkoRepussa(esine):
    if esine in pelaaja['reppu']:
        return True
    else:
        printText(f'{esine.upper()} ei ole repussasi.')
        return False

def showStart():
    print("Majatalon isäntä on huhuillut sinut sisään. Hän vaikuttaa hermostuneelta.")

def showStory():
    print(f"{paikat[pelaaja['paikkaIndeksi']]['tarina']}")

def checkWhere(indeksi):
    printText(f"Olet paikassa {pelaaja['paikka'].upper()}.")
    printText(f'Täällä on {paikat[indeksi]['hahmot']}.')
    printText(f'Hän sanoo: {paikat[indeksi]['puhe']}!')
    printText('Voit kysyä häneltä seuraavia asioita:' )

    asiat = list(epht[paikat[indeksi]['hahmot']])
    printattavat = len(asiat) -2

    for i in range(printattavat):
        printText(CGREEN + asiat[i] + CEND)

    print()

    if len(paikat[indeksi]['esineet'])> 0:
        printText("Täältä löytyy: ")
        for esine in paikat[indeksi]['esineet']:
            printText(esine)
        print()
    else:
        printText("Huoneessa ei ole poimittavia esineitä.")

def checkItem(item):
    print(f'{esineet[item]['kuvaus']}')


def setPlayerPlace(place, index):
    pelaaja['paikka'] = place
    pelaaja['paikkaIndeksi'] = index


def addToIventory(item, placeIndex):
    if item in paikat[placeIndex]['esineet'].keys():
        pelaaja['reppu'].append(item)
        paikat[placeIndex]['esineet'].pop(item)
        printText(f'{esineet[item]['synonyymi'].upper()} lisätty reppuun!')
        print()
    else:
        printText(f'Esinettä {item} ei löydy täältä.')

def removeFromInventory(item):
    epht[paikat[pelaaja['paikkaIndeksi']]['hahmot']]['esineet'].append(item)
    pelaaja['reppu'].remove(item)

def checkInventory():
    if len(pelaaja['reppu']) > 0:
        printText("Repussasi on:")
        for item in pelaaja['reppu']:
            printText(CGREEN + esineet[item]['synonyymi'].upper() + CEND)
    else:
        printText('Reppusi on tyhjä.')
    print()

def tellMeMore(question, index):
    hahmo = paikat[index]['hahmot']
    print(f'{hahmo.capitalize()} sanoo "{epht[hahmo][question]}"')

def checkForDeath(place, index):
    if place == 'kellari' and 'lamppu' not in pelaaja['reppu']:
        printText(f'Sinut söi kamala {paikat[index]['hahmot']}!')
        printText(f'{paikat[index]['puhe']}')
        return True
    elif place == 'kellari' and 'lamppu' in pelaaja['reppu']:
        printText(f'Lamppu pelasti sinut kamalan {paikat[index]['hahmot']}n kynsistä. HUH! ')
        return False

def tarkistaHaluaako(esine, haluttuEsine):
    if esine == haluttuEsine:
        return True
    else:
        return False

def tarkistaVoitto():
    if 'kirja' in epht['isäntä']['esineet']:
        return True
    else:
        return False

def tarkistaTyhmyys():
    if 'lamppu' in epht['grue']['esineet']:
        return True
    else:
        return False

def unableToExecute():
    printText('Anteeksi, en ymmärtänyt.')
    print()

def printText(string):
    for char in string:
        print(char, end='', flush=True)
        time.sleep(.05)
    print()

def convertToBasicForm(place):
    if place == 'tupaan':
        return 'tupa'
    elif place == 'kellariin':
        return 'kellari'

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
            printText(epht[paikat[pelaaja['paikkaIndeksi']]['hahmot']]['esineet'])
            print()
    elif sanaMaara == 1:
        unableToExecute()
    elif sanaMaara == 2:
        verbi = komentoLista[0]
        substantiivi = komentoLista[1]

        try:
            if (verbi == ottaa['ota']) and substantiivi in ottaa['otettavat']:
                paikkaIndeksi = pelaaja['paikkaIndeksi']
                addToIventory(substantiivi, paikkaIndeksi)

            elif (verbi == 'avaa' and substantiivi == 'reppu'):
                checkInventory()

            elif(verbi == kuvaile['kuvaile'] and substantiivi in kuvaile['kuvailtavat']):
                if substantiivi == 'paikka':
                    paikkaIndeksi = pelaaja['paikkaIndeksi']
                    checkWhere(paikkaIndeksi)
                else:
                    checkItem(substantiivi)

            elif(verbi == menna['mene'] and substantiivi in menna['mentavat']):
                substantiivi = convertToBasicForm(substantiivi)
                paikkaIndeksi = checkIndex(substantiivi)
                setPlayerPlace(substantiivi, paikkaIndeksi)
                printText(paikat[paikkaIndeksi][substantiivi].upper())
                printText(paikat[paikkaIndeksi]['tarina'])
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

    if(tarkistaTyhmyys()):
        print('Ei voi olla totta!')
        print('Miksi teit noin. Nyt grue syö sinut!')
        break

    if(tarkistaVoitto()):
        print('Huikeaa, isäntä sai kirjansa ja pääsee noitumaan!')
        print('Olet voittanut!')
        break

    komento = input('Mitä teet?> ').strip().lower()


printText(f'Ensi kertaan! Lopulliset pisteesi ovat: {pelaaja["pisteet"]} / {maksimiPisteet}.')


