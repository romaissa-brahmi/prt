from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime
import time

f = open("ppRawData.txt", "a", encoding='utf8')

i = 0

while (i < 36):
    browser = webdriver.Safari()

    browser.get("https://pubs.diabox.com/diaboxStaticView.php?id=105")
    html = browser.page_source
    time.sleep(3)
    browser.close()

    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find(id="livegaugeArea").text

    indexWINDbeginning = data.find("Vent")
    indexWINDending = data.find("Hum")
    rawData = data[indexWINDbeginning + 4: indexWINDending]

    windDirection = (rawData[29: 35])
    windSpeed = (rawData[76: 81])

    f.writelines(str(datetime.today().day) + "-" + str(datetime.today().month) + " ")
    f.writelines(str(datetime.today().hour) + " ")
    f.writelines(windSpeed + " ")
    f.writelines(windDirection + " ")
    f.writelines("\n")

    i += 1

    # décider si toutes les 5min(300) ou toutes les 10min(600)
    time.sleep(300)

f.close()
