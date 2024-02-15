from datetime import datetime, timedelta

syncWG = []

f = open("wgData.txt", "r", encoding='utf8')
wgData = f.readlines()
f.close()

f = open("ppData.txt", "r", encoding='utf8')
ppData = f.readlines()
f.close()

for eachWgData in wgData:
    found = False
    day = False
    if int(eachWgData[0:2]) == datetime.today().day or int(eachWgData[0:2]) == (datetime.today() + timedelta(1)).day:
        day = True
    for eachPpData in ppData:
        if eachPpData[0:8] == eachWgData[0:8]:
            found = True
    if day or found :
        syncWG.append(wgData[wgData.index(eachWgData)])


f = open("wgData2.txt", "w", encoding='utf8')
for i in range(len(syncWG)):
    f.writelines(syncWG[i])
f.close()
