import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

PATH = 'C:\Program Files (x86)\chromedriver.exe'
PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
target_url = "https://www.zillow.com/homes/for_sale/Brooklyn,-New-York,-NY_rb/"

l=list()
obj={}

driver=webdriver.Chrome(PATH)
driver.get(target_url)

html = driver.find_element(By.TAG_NAME, 'html')
html.send_keys(Keys.END)

time.sleep(5)
resp = driver.page_source
driver.close()

soup=BeautifulSoup(resp,'html.parser')
properties = soup.find_all("div",{"class":"StyledPropertyCardDataWrapper-c11n-8-69-2__sc-1omp4c3-0 KzAaq property-card-data"})

for x in range(0,len(properties)):
        try:
            obj["pricing"]=properties[x].find("div",{"class":"StyledPropertyCardDataArea-c11n-8-69-2__sc-yipmu-0 kJFQQX"}).text
        except:
            obj["pricing"]=None
        try:
            obj["size"]=properties[x].find("div",{"class":"StyledPropertyCardDataArea-c11n-8-69-2__sc-yipmu-0 bKFUMJ"}).text
        except:
            obj["size"]=None
        try:
            obj["address"]=properties[x].find("a",{"class":"StyledPropertyCardDataArea-c11n-8-69-2__sc-yipmu-0 dZxoFm property-card-link"}).text
        except:
            obj["address"]=None
        l.append(obj)
        obj={}
print(l)
