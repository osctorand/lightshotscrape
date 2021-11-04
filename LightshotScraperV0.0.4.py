#Importer
import requests
import random
import string
from bs4 import BeautifulSoup 
import cloudscraper
import threading
import time
import os
import base64
#CLI-Introduktion och konfiguration
print("Välkommen till ett program som automatiskt letar igenom och laddar ner bilder från prnt.sc.")
print("Konfiguration: ")

#Konfiguration för programmet.
arbetskraft = int(input("\nHur många trådar ska programmet använda?: "))
location = input("\nVar ska bilderna sparas?: ")

#laddar exempelbild för att jämföra borttagna bilder.

def Process():
    while True:
        while True:
            links = None
            stringlist = None
            item = None
            imagelink = None
            os.system("cls")
            print("\nArbetar...")
            code = []

            #Väljer automatiskt en länk uppbyggd av 6 slumpmässiga bokstäver och siffror.
            for i in range(6):

                #"Selector" är vad som bestämmer om nästa siffra ska vara en siffra eller en bokstav.
                selector = random.randint(1,2)

                #"Chars" är bokstäver.
                chars = random.choice(string.ascii_lowercase)

                #"Numbers" är nummer.
                numbers = random.choice(list(string.hexdigits[0:10]))

                #Om "selector" blir 1 så välojs en bokstav, och om den blir 2 så väljs en siffra. Bokstäverna läggs sedan in i en lista.
                if selector == 1:
                    code.append(chars)
                if selector == 2:
                    code.append(numbers)

            #Listan sätts ihop till en string.
            codestr = ''.join(code)

            #URLen byggs upp av domänen och de slumpmässiga siffrorna/bokstäverna.
            URL = "https://prnt.sc/" + str(codestr)


            #Skapar webscrapern. Anvnder cloudscraper för att komma igenom cloudflaren anti-bot filter.
            scraper = cloudscraper.create_scraper()


            try:

                #Mer CLI-text för användervänlighet.
                print("bearbetar länk " + str(URL))

                #Fångar hela sidan som HTML-text.
                site = scraper.get(URL).text

                #Startar BS4 för att leta igenom HTML-text.
                soup = BeautifulSoup(site, "html.parser")

                #Skapar "Stringlist", som senare ska hålla URL som hittas på sidan.
                stringlist = []

                #BS4 Letar igenom sidan för element med taggen "img".
                for item in soup.find_all('img'):

                    #Sparar alla "scr" element i taggen "img", altså alla bildlänkar för bilder.
                    links = item['src']

                    #Lägger alla dessa URL i "stringlist"
                    stringlist.append(links)

                #Mer CLI-användervänlighet.
                print("Hittade bildlänk!: " + str(stringlist[0]))

            #Om någonting går fel skickas ett felmeddelande, men programmet fortsätter att repetera.
            except Exception:
                print("cloudflare blockerade förfrågan.")



            #BS4 hittar vanligvis 3 bild-URL. Den första är då bilden vi letar efter. Den sparar därför första länken som "imagelink"
            try:
                imagelink = requests.get(stringlist[0], stream=True, allow_redirects=True,timeout=1000000)
            except Exception:
                print("Hittade falsk bild, fortsätter till borttagning... ")
                pass

            #Om cloudscraper går in på en länk där det inte finns en bild, kommer stringlist[0] alltid vara samma länk. Filtrerar därför ut just den länken och skickar ett felmeddelande.
            if stringlist[0] == '//st.prntscr.com/2021/10/22/2139/img/footer-logo.png':
                print("Hittade falsk bild, fortsätter...")


            #Hittar filnamnstillägget på bilden genom att kolla på de sista 3 bokstäverna i bildlänken.
            imagestring = stringlist[0]
            extension = imagestring[-3:]

            #Sparar filnamnstillägget som PNG om bildlänken slutar med PNG.
            if extension == 'png':
                ext = "png"
                print("Hittade PNG! Sparar...")

            #Sparar filnamnstillägget som JPG om bildlänken slutar med JPG eller JPEG.
            if extension == 'jpg' or extension == "jpeg":
                ext = "jpg"
                print("Hittade JPG! Sparar...")


            #Skapar en fil som antingen är PNG eller JPG beroende på ext (filnamnstillägget)
            with open(str(location) + "/" + str(codestr) + "." + ext, "wb") as handler:
                #Sparar bilden i filen.
                try:
                    handler.write(imagelink.content)

                #Om det inte fungerar är bildlänken korrupt, och programmet tar sedan bort bilden och återställer värdena på programmet.
                except Exception:
                    print("Bildlänk var inte verklig. Tar bort bild...")
                    handler.close()
                    os.unlink(str(location) + "/" + str(codestr) + "." + ext)
                    break

                handler.close()

            #Öppnar den nyligen sparade filen igen och läser den första raden av text i filen. Konverterar även bilden till base64.
            with open(str(location) + "/" + str(codestr) + "." + ext) as reader:
                print("Kontrollerar om bilden är riktig...")
                try:
                    korrupt = 0
                    imagefiletext = reader.readlines(1)
                    korrupt = 1
                except:
                    print("Bild kontrollerad.")

                reader.close()


            #Om första raden av text i filen är det innebär det att det inte var en bild som sparades, utan ett CloudFlare-felmeddelande.
            if korrupt == 1:
                print("Hittade korrupt fil!")

                #Försöker därför ta bort filen.
                try:
                    os.unlink(str(location) + "/" + str(codestr) + "." + ext)
                    print("Tog bort korrupt fil.")

                #Om det inte går, meddela användaren.
                except Exception:
                    print("Kunde inte ta bort korrupt fil!")
                    raise Exception

            #Kontrollerar om bilden är imgurs "image removed"-bild genom att kolla storleken på bilden.
            if korrupt == 0:
                print("Kontrollerar om bild redan är borttagen...")
                try:
                    filesize = os.path.getsize(str(location) + "/" + str(codestr) + "." + ext)
                    if filesize < 510:
                        os.unlink(str(location) + "/" + str(codestr) + "." + ext)
                        print("Tog bort borttagen bild")
                    else:
                        print("Bild var inte borttagen. Sparar...")

                #Om det inte går, meddela användaren.
                except Exception:
                    print("Kunde inte ta bort borttagen fil!")
                    raise Exception

            #Vänta i 2 sekunder för att förhindra att bli bannad.
            time.sleep(2)
        time.sleep(2)


#Början på trådar.
threads = []

#Skapar n antal trådar beroende på vad användaren skrev i konfigurationen.
for i in range(arbetskraft):
    t = threading.Thread(target=Process)
    t.daemon = True
    threads.append(t)

for i in range(arbetskraft):
    threads[i].start()

for i in range(arbetskraft):
    threads[i].join()