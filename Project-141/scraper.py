from selenium import webdriver
from bs4 import BeautifulSoup
import time, csv
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests

star_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get(star_url)
time.sleep(10)
star_list=[]
star_data_full=[]
headers=["Name","Distance","Mass","Radius"]

def scraper():
    soup=BeautifulSoup(browser.page_source,"html.parser")
    templist=[]
    for row in soup.find_all("tr"):
        for tdtags in row.find_all("td"):

            templist.append(tdtags.find_all("a").title)
            #templist.append(tdtags.contents[0])
    
    print(templist)

scraper()