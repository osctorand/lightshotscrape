import requests
import random
import string
from bs4 import BeautifulSoup 
import cloudscraper
import time
import os
import sys
import getopt

scraper = cloudscraper.create_scraper()

def ImageLinkGenerator():
    #Genererar en slumpad länk
    linkEnd = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(12))
    link = "https://prnt.sc/" + linkEnd
    return link

def ImageHandler(link):
    try:
        scraper = cloudscraper.create_scraper()
        site = scraper.get(link).text
        soup = BeautifulSoup(site, 'html.parser')
        img = soup.find_all('img')[0]
        img = img['src']
        return img
    except Exception as e:
        print(e)

def ImageVerifier(img):
    pass

print("test",file=sys.stdout)
