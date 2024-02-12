from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime
import time

f = open("ppRawData.txt", "a", encoding='utf8')

i = 0

browser = webdriver.Chrome()

while (i < 3):
    browser.get("https://pubs.diabox.com/diaboxStaticView.php?id=105")
    time.sleep(10)
    html = browser.page_source

    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find(id="livegaugeArea").text

    indexWINDbeginning = data.find("Vent")
    indexWINDending = data.find("Hum")
    rawData = data[indexWINDbeginning + 5: indexWINDending]
    dataList = rawData[29:81].split(" °Temps réel\n\n\nCreated with Raphaël 2.1.2\n")

    windDirection = dataList[0].split(" ")[0]
    windSpeed = dataList[1].split(" ")[0]

    response = str(datetime.today().day) + "-" + str(datetime.today().month) + " " + str(
        datetime.today().hour) + " " + windSpeed + " " + windDirection
    f.writelines(response + "\n")
    i += 1

f.close()
browser.close()
