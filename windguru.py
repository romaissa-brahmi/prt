import requests
from bs4 import BeautifulSoup

url = "https://old.windguru.cz/fr/index.php?sc=48617"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

 
divClass = soup.find(id="div_wgfcst2")

text = ""
for each in divClass:
    text += each.text

indexWINDSPD = text.find("WINDSPD")
rawWINDSPD = text[indexWINDSPD+10 : indexWINDSPD+600]

indexFin = rawWINDSPD.find("]")
rawWINDSPD = rawWINDSPD[ : indexFin]
print(rawWINDSPD)

WINDSPDlist = rawWINDSPD.split(",")
print(WINDSPDlist)

for each in WINDSPDlist :
    each = float(each)
print(WINDSPDlist)


indexWINDDIR = text.find("WINDDIR")
rawWINDDIR = text[indexWINDDIR+10 : indexWINDDIR+550]
indexFin = rawWINDDIR.find("]")
rawWINDDIR = rawWINDDIR[ : indexFin]

print(rawWINDDIR)

WINDDIRlist = rawWINDDIR.split(",")
print(WINDDIRlist)

for each in WINDDIRlist :
    each = float(each)
print(WINDDIRlist)






#pour arrondir = (+22.5)

directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSO", "SO", "OSO", "O", "ONO", "NO", "NNO"]












