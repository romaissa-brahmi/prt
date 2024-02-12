from bs4 import BeautifulSoup
from selenium import webdriver
import time

browser=webdriver.Chrome()

browser.get("https://pubs.diabox.com/diaboxStaticView.php?id=105")
time.sleep(10)
html = browser.page_source
browser.close()


soup = BeautifulSoup(html, 'html.parser')
data = soup.find(id="livegaugeArea").text


indexWINDbeginning = data.find("Vent")
indexWINDending = data.find("Hum")
rawData = data[indexWINDbeginning + 5: indexWINDending]
dataList = rawData[29:81].split(" °Temps réel\n\n\nCreated with Raphaël 2.1.2\n")

windDirection = dataList[0].split(" ")[0]
windSpeed = dataList[1].split(" ")[0]

print(windDirection)
print(windSpeed)
