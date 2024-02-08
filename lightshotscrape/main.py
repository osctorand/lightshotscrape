#Importer
import requests
import random
import string
from bs4 import BeautifulSoup 
import cloudscraper
import time
import os
import sys
import getopt

nameargv = sys.argv[1:]

try:
    opts = getopt.getopt(nameargv, "m:", ["mode ="])
    #lets's check out how getopt parse the arguments
    print(opts)
except:
    print("Ange inställning ('-m en' eller '-m loop')")
    sys.exit(2)


#Anger sökväg för att spara bildern
#imgpath = input("Var ska bilderna sparas? (Enter för att spara i Sparade Bilder)").strip() or "C:\\Users\\%username%\\Pictures\\Saved Pictures"
imgpath = "C:\\Users\\%username%\\Pictures\\Saved Pictures"


##scraper
scraper = cloudscraper.create_scraper()


##image handler




#   Bz_iVlFAetPw
#   0IhIfZmMIaeK
#   DzkuQXuxfW5-
