from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime
import time

'''
f = open("ppRawData.txt", "a", encoding='utf8')

i = 0

browser = webdriver.Chrome()
browser.get("https://pubs.diabox.com/diaboxStaticView.php?id=105")

while i < 60:
    print(i)
    time.sleep(120)
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
    print(response)

    i += 1

f.close()
browser.close()

'''
f = open("ppRawData.txt", "r", encoding='utf8')
L = f.readlines()
f.close()

meanSpeed = 0
meanDirection = 0

for i in range(len(L)):

    value = L[i].split(" ")
    print(value)

    meanSpeed += float(value[2])
    meanDirection += float(value[3])

print(meanSpeed / len(L))
print(meanDirection / len(L))

f = open("ppData.txt", "a", encoding='utf8')
f.writelines(str(datetime.today().day) + "-" + str(datetime.today().month) + " ")
f.writelines(str(datetime.today().hour) + " ")
f.writelines("%.1f" % (meanSpeed / len(L)) + " ")
f.writelines("%.1f" % (meanDirection / len(L)) + " ")
f.writelines("\n")
f.close()
