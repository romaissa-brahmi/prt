from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://pubs.diabox.com/diaboxStaticView.php?id=105")
time.sleep(120)
elements = driver.find_elements(By.CLASS_NAME, 'livegaugeArea')
print(elements)
driver.quit()


"""

f = open("ppRawData.txt", "w", encoding='utf8')

i = 0
while i < 35:
    print(i)
    time.sleep(120)

    indexWINDbeginning = data.find("Vent")
    indexWINDending = data.find("Hum")
    rawData = data[indexWINDbeginning + 5: indexWINDending]
    dataList = rawData[29:81].split(" °Temps réel\n\n\nCreated with Raphaël 2.1.2\n")

    windDirection = dataList[0].split(" ")[0]
    windSpeed = dataList[1].split(" ")[0]

    response = str(datetime.today().day) + "-" + str(datetime.today().month) + " " + str(
        datetime.today().hour) + " " + windSpeed + " " + windDirection
    f.writelines(response + "\n")
    print(response)

    i += 1

f.close()
"""
