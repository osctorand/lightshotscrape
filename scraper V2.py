import requests
import random
import string
from bs4 import BeautifulSoup 
import cloudscraper
import threading
import time
import os

print("Välkommen till ett program som automatiskt letar igenom och laddar ner bilder från prnt.sc.")

print("Konfiguration: ")

arbetskraft = int(input("\nHur många trådar ska programmet använda?: "))
location = input("\nVar ska bilderna sparas?: ")


def Process():
    while True:
        print("\nArbetar...")
        code = []

        for i in range(6):
            selector = random.randint(1,2)
            chars = random.choice(string.ascii_lowercase)
            numbers = random.choice(list(string.hexdigits[0:10]))

            if selector == 1:
                code.append(chars)
            if selector == 2:
                code.append(numbers)

        codestr = ''.join(code)
        URL = "https://prnt.sc/" + str(codestr)

        scraper = cloudscraper.create_scraper()
        try:
            print("bearbetar länk " + str(URL))
            site = scraper.get(URL).text
            soup = BeautifulSoup(site, "html.parser")
            stringlist = []
            for item in soup.find_all('img'):
                links = item['src']
                stringlist.append(links)
            print(stringlist[0])

        except Exception:
            print("cloudflare blockerade förfrågan.")
            pass

        try:
            imagelink = requests.get(stringlist[0], stream=True, allow_redirects=True,timeout=1000000)
            if stringlist[0] == '//st.prntscr.com/2021/10/22/2139/img/footer-logo.png':
                print("Hittade falsk bild, fortsätter...")
                pass

            imagestring = stringlist[0]
            extension = imagestring[-3:]

            if extension == 'png':
                ext = "png"
                print("Hittade PNG! Sparar...")
                
            if extension == 'jpg' or extension == "jpeg":
                ext = "jpg"
                print("Hittade JPG! Sparar...")
            else:
                pass

            with open(str(location) + "/" + str(codestr) + "." + ext, "wb") as handler:
                handler.write(imagelink.content)
                handler.close
            
            with open(str(location) + "/" + str(codestr) + "." + ext) as reader:
                imagefiletext = reader.readlines(1)
                reader.close

            if imagefiletext[0] == "<!DOCTYPE html>\n":
                print("Hittade korrupt fil!")
                try:
                    os.unlink(str(location) + "/" + str(codestr) + "." + ext)
                    print("Tog bort korrupt fil.")
                except Exception:
                    print("Kunde inte ta bort korrupt fil!")
                    raise Exception


        except Exception:
            pass

        time.sleep(2)

threads = []

for i in range(arbetskraft):
    t = threading.Thread(target=Process)
    t.daemon = True
    threads.append(t)

for i in range(arbetskraft):
    threads[i].start()

for i in range(arbetskraft):
    threads[i].join()