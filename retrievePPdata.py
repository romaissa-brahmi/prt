import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time

service = Service(executable_path=r'/snap/chromium/2768/usr/lib/chromium-browser/chromedriver')
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://pubs.diabox.com/diaboxStaticView.php?id=105")
time.sleep(30)
elements = driver.find_element(By.XPATH, "/html/body").text
driver.quit()

indexWINDbeginning = elements.find("WIND")
indexWINDending = elements.find("HUM")
rawData = elements[indexWINDbeginning + 32: indexWINDending - 15]

dataList = rawData.split(" °\nRealtime\nCreated with Raphaël 2.1.2\n")

windDirection = dataList[0].split(" ")[0]
windSpeed = dataList[1].split(" ")[0]

today = str(datetime.today().day)
if len(today) == 1:
    today = "0" + today

data = today + "-" + str(datetime.today().month) + " " + str(
    datetime.today().hour) + " " + windSpeed + " " + windDirection

file = "/home/ubuntu/prt/" + today + "-" + str(datetime.today().month) + "-PacificPalissadesData.txt"
os.system("echo '{}' >> 14-3-PacificPalissadesData.txt".format(data))
