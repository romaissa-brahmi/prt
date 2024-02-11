from bs4 import BeautifulSoup
from selenium import webdriver
import time

browser=webdriver.Safari()

browser.get("https://pubs.diabox.com/diaboxStaticView.php?id=105")
html = browser.page_source
time.sleep(3)
browser.close()


soup = BeautifulSoup(html, 'html.parser')
data = soup.find(id="livegaugeArea").text


indexWINDbeginning = data.find("Vent")
indexWINDending = data.find("Hum")
rawData = data[indexWINDbeginning + 4: indexWINDending]

windDirection = float(rawData[29 : 35])
windSpeed = float(rawData[76 : 81])

print(windDirection)
print(windSpeed)
