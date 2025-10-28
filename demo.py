import time

paikat = [
        {'tupa' :'tupa',
         'tarina': 'Olet vanhassa hollituvassa.',
        'esineet': {'avain': 'avain', 'lamppu': 'lamppu'},
        'indeksi': 0},
        {'kellari': 'kellari',
         'tarina': 'Onpa täällä pimeää. Hui! Siunt todennäköisesti syö grue.',
         'esineet': {'kirja': 'kirja'},
         'indeksi': 1
        }
]

tupa = paikat[0]
kellari = paikat[1]

coms = [
    {'ota':'ota',
     'otettavat' : {'lamppu': 'lamppu', 'avain': 'avain'}
    },
    {
    'avaa': 'avaa',
    'avattavat': {'ovi': 'ovi', 'reppu': 'reppu'}
    },
    {'kerro': 'kerro',
    'kerrottavat': {'paikka': 'paikka'}
    },
    {'mene': 'mene',
     'mentavat': {'tupa': 'tupa', 'kellari': 'kellari'}}
]

ottaa = coms[0]
avata = coms[1]
kertoa = coms[2]
menna = coms[3]



pelaaja = {'pisteet':0,
           'paikka' : 'tupa',
           'paikkaIndeksi': 0,
           'reppu': []}

def checkIndex(place):
    if place == 'tupa':
        return 0
    elif place == 'kellari':
        return 1

def showStart():
    print("jepu jee peli alkaa")

def showStory():
    print(f"{paikat[pelaaja['paikkaIndeksi']]['tarina']}")

def checkWhere(indeksi):

    printText(f"Olet paikassa {pelaaja['paikka'].upper()}.")
    if len(paikat[indeksi]['esineet'])> 0:
        printText("Täältä löytyy: ")
        for esine in paikat[indeksi]['esineet']:
            printText(esine)
        print()
    else:
        printText("Huone on tyhjä.")

def setPlayerPlace(place, index):
    print(index)
    pelaaja['paikka'] = place
    pelaaja['paikkaIndeksi'] = index


def addToIventory(item):
    pelaaja['reppu'].append(item)
    tupa['esineet'].pop(item)
    printText(f'{item.upper()} lisätty reppuun!')
    print()

def checkInventory():
    printText("Repussasi on:")
    for item in pelaaja['reppu']:
        printText(item.upper())
    print()

def unableToExecute():
    printText('Anteeksi, en ymmärtänyt.')
    print()

def printText(string):
    for char in string:
        print(char, end='', flush=True)
        time.sleep(.08)
    print()

sanaMaara = 0
showStart()
showStory()
komento = input("Mitä teet?> ").strip()

for item in komento.split(" "):
        sanaMaara = sanaMaara + 1;

while komento != 'Lopeta':
    komentoLista = komento.split(" ")
    if sanaMaara == 1 and komento == 'apua':
            printText('Apua saa täältä!')
            print()
    elif sanaMaara == 1:
        unableToExecute()
    elif sanaMaara == 2:
        verbi = komentoLista[0]
        substantiivi = komentoLista[1]

        try:
            if (verbi == ottaa['ota']) and substantiivi == ottaa['otettavat'][substantiivi]:
                addToIventory(substantiivi)
            elif (verbi == avata['avaa'] and substantiivi == avata['avattavat']['reppu']):
                checkInventory()
            elif(verbi == kertoa['kerro'] and substantiivi == kertoa['kerrottavat']['paikka']):
                paikkaIndeksi = pelaaja['paikkaIndeksi']['indeksi']
                checkWhere(paikkaIndeksi)
            elif(verbi == menna['mene'] and substantiivi == menna['mentavat'][substantiivi]):
                paikkaIndeksi = checkIndex(substantiivi)
                indeksi = paikat[paikkaIndeksi]
                setPlayerPlace(substantiivi, indeksi)

            else:
                unableToExecute()
        except:
            print("kaatuu")
    else:
        unableToExecute()


    komento = input("Anna komento (kirjoita 'Lopeta' poistuaksesi): ").strip()





