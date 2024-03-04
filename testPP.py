import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time

os.system("date >> /home/ubuntu/prt/PacificPalissadesData.txt")

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://pubs.diabox.com/diaboxStaticView.php?id=105")
time.sleep(10)
elements = driver.find_element(By.XPATH, "/html/body").text
driver.quit()

indexWINDbeginning = elements.find("VENT")
indexWINDending = elements.find("HUM")
rawData = elements[indexWINDbeginning + 32: indexWINDending - 17]

dataList = rawData.split(" °\nTemps réel\nCreated with Raphaël 2.1.2\n")

windDirection = dataList[0].split(" ")[0]
windSpeed = dataList[1].split(" ")[0]

today = str(datetime.today().day)
if len(today) == 1:
    today = "0" + today

data = today + "-" + str(datetime.today().month) + " " + str(
    datetime.today().hour) + " " + windSpeed + " " + windDirection
print(data)

os.system("echo '{}' >> /home/ubuntu/prt/PacificPalissadesData.txt".format(data))

