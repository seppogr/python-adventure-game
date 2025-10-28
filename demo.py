import time
import os

paikat = [
        {'tupa' :'tupa',
         'tarina': 'Olet vanhassa hollituvassa.',
        'esineet': {'avain': 'avain', 'lamppu': 'lamppu'},
        'hahmot': 'isäntä',
        'puhe' : 'Kellarissa on grue. Varo ettei se popsaise sinua suihinsa!'
        },
        {'kellari': 'kellari',
         'tarina': 'Onpa täällä pimeää. Hui! Siut todennäköisesti syö grue.',
         'esineet': {'kirja': 'kirja'},
         'hahmot' : 'grue',
         'puhe' : 'Maiskis!'
        }
]

tupa = paikat[0]
kellari = paikat[1]

coms = [
    {'ota':'ota',
     'otettavat' : {'lamppu': 'lamppu', 'avain': 'avain', 'kirja': 'kirja'}
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



pelaaja = {'pisteet': 0,
           'paikka' : '',
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
    #trimmedPlayer = pelaaja['paikka'][:-2]
    printText(f"Olet paikassa {pelaaja['paikka'].upper()}.")
    printText(f'Täällä on {paikat[indeksi]['hahmot']}')
    printText(f'Hän sanoo: {paikat[indeksi]['puhe']}')
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


def addToIventory(item, placeIndex):
    if item in paikat[placeIndex]['esineet'].keys():
        pelaaja['reppu'].append(item)
        paikat[placeIndex]['esineet'].pop(item)
        printText(f'{item.upper()} lisätty reppuun!')
        print()
    else:
        printText(f'Esinettä {item} ei löydy täältä.')

def checkInventory():
    printText("Repussasi on:")
    for item in pelaaja['reppu']:
        printText(item.upper())
    print()

def checkForDeath(place, index):
    if place == 'kellari' and 'lamppu' not in pelaaja['reppu']:
        printText(f'Sinut söi kamala {paikat[index]['hahmot']}!')
        printText(f'{paikat[index]['puhe']}')
        return True
    elif place == 'kellari' and 'lamppu' in pelaaja['reppu']:
        printText(f'Lamppu pelasti sinut kamalan {paikat[index]['hahmot']}n kynsistä. HUH! ')
        return False

def unableToExecute():
    printText('Anteeksi, en ymmärtänyt.')
    print()

def printText(string):
    for char in string:
        print(char, end='', flush=True)
        time.sleep(.08)
    print()


showStart()
showStory()
setPlayerPlace(menna['mentavat']['tupa'], 0)
komento = input('Mitä teet?> ').strip()


while komento != 'Lopeta':
    sanaMaara = 0
    for item in komento.split(" "):
        sanaMaara = sanaMaara + 1

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
                paikkaIndeksi = pelaaja['paikkaIndeksi']
                addToIventory(substantiivi, paikkaIndeksi)

            elif (verbi == avata['avaa'] and substantiivi == avata['avattavat']['reppu']):
                checkInventory()

            elif(verbi == kertoa['kerro'] and substantiivi == kertoa['kerrottavat']['paikka']):
                paikkaIndeksi = pelaaja['paikkaIndeksi']
                checkWhere(paikkaIndeksi)

            elif(verbi == menna['mene'] and substantiivi == menna['mentavat'][substantiivi]):
                paikkaIndeksi = checkIndex(substantiivi)
                setPlayerPlace(substantiivi, paikkaIndeksi)
                printText(paikat[paikkaIndeksi][substantiivi].upper())
                printText(paikat[paikkaIndeksi]['tarina'])
                if (checkForDeath(substantiivi, paikkaIndeksi)):
                    printText('Voi sentään. Kuolit. Peli päättyi.')
                    break
            else:
                unableToExecute()
        except:
            print(f'kaatuu: "{verbi}" tai "{substantiivi}" ei ole tuettujen komentojen joukossa. Kirjoita "apua" nähdäksesi sallitut komennot.')
    else:
        unableToExecute()


    komento = input('Mitä teet?> ').strip()





