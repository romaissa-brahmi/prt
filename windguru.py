from datetime import datetime
import requests
from bs4 import BeautifulSoup

url = "https://old.windguru.cz/fr/index.php?sc=48617"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

 
divClass = soup.find(id="div_wgfcst2")

text = ""
for each in divClass:
    text += each.text


# DATE DU JOUR
indexDay = text.find("hr_d")
rawDate = text[indexDay+63 : indexDay+85]

Datelist = rawDate.split("\",\"")
for each in Datelist:
   each = int(each)

month = str(datetime.today().month)

# HEURE DU JOUR
indexHour = text.find("hr_h")
rawHour = text[indexHour+63 : indexHour+85]

Hourlist = rawHour.split("\",\"")
for each in Hourlist:
   each = int(each)


# VITESSE DU VENT
indexWINDSPD = text.find("WINDSPD")
rawWINDSPD = text[indexWINDSPD+10 : indexWINDSPD+600]

indexFin = rawWINDSPD.find("]")
rawWINDSPD = rawWINDSPD[ : indexFin]

WINDSPDlist = rawWINDSPD.split(",")
WINDSPDlist = WINDSPDlist[11:16]

for each in WINDSPDlist:
    each = float(each)


# DIRECTION DU VENT
indexWINDDIR = text.find("WINDDIR")
rawWINDDIR = text[indexWINDDIR+10 : indexWINDDIR+550]
indexFin = rawWINDDIR.find("]")
rawWINDDIR = rawWINDDIR[ : indexFin]

WINDDIRlist = rawWINDDIR.split(",")
WINDDIRlist = WINDDIRlist[11:16]

for each in WINDDIRlist:
    each = int(each)


f = open("wgData.txt", "a", encoding='utf8')

for i in range(5):
    f.writelines(Datelist[i] + "-" + month + " ")
    f.writelines(Hourlist[i] + " ")
    f.writelines(WINDSPDlist[i] + " ")
    f.writelines(WINDDIRlist[i] + " ")
    f.writelines("\n")

f.close()



directionNames = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSO", "SO", "OSO", "O", "ONO", "NO", "NNO"]
directionDegrees = [0.0, 22.5, 45.0, 67.5, 90.0, 112.5, 135.0, 157.5, 180.0, 202.5, 225.0, 247.5, 270.0, 292.5, 315.0, 337.5, 360.0]












