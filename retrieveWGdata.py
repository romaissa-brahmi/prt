import os
from datetime import datetime, timedelta
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
rawDate = text[indexDay + 8: indexDay + 85]
Datelist = rawDate.split("\",\"")
for each in Datelist:
    each = int(each)


# HEURE DU JOUR
indexHour = text.find("hr_h")
rawHour = text[indexHour + 8: indexHour + 85]

Hourlist = rawHour.split("\",\"")
for each in Hourlist:
    each = int(each)


# VITESSE DU VENT
indexWINDSPD = text.find("WINDSPD")
rawWINDSPD = text[indexWINDSPD + 10: indexWINDSPD + 600]

indexFin = rawWINDSPD.find("]")
rawWINDSPD = rawWINDSPD[: indexFin]

WINDSPDlist = rawWINDSPD.split(",")
WINDSPDlist = WINDSPDlist[0:16]

for each in WINDSPDlist:
    each = float(each)


# DIRECTION DU VENT
indexWINDDIR = text.find("WINDDIR")
rawWINDDIR = text[indexWINDDIR + 10: indexWINDDIR + 550]
indexFin = rawWINDDIR.find("]")
rawWINDDIR = rawWINDDIR[: indexFin]

WINDDIRlist = rawWINDDIR.split(",")
WINDDIRlist = WINDDIRlist[0:16]

for each in WINDDIRlist:
    each = int(each)

data = ""
tomorrow = str((datetime.today() + timedelta(1)).day)
if len(tomorrow) == 1:
    tomorrow = "0" + tomorrow
month = str(datetime.today().month)


for i in range(len(Datelist)):
    if Datelist[i] == tomorrow and 4 <= int(Hourlist[i]) <= 22:
        data += (Datelist[i] + "-" + month + " ")
        data += (Hourlist[i] + " ")
        data += (WINDSPDlist[i] + " ")
        data += (WINDDIRlist[i] + " ")
        data += "\n"

os.system("echo '{}' >> /home/ubuntu/prt/WindguruData.txt".format(data))

# directionNames = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSO", "SO", "OSO", "O", "ONO", "NO", "NNO"]
# directionDegrees = [0.0, 22.5, 45.0, 67.5, 90.0, 112.5, 135.0, 157.5, 180.0, 202.5, 225.0, 247.5, 270.0, 292.5, 315.0, 337.5, 360.0]
