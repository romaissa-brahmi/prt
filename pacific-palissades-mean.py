from datetime import datetime

f = open("ppRawData.txt", "r", encoding='utf8')
L = f.readlines()
f.close()

meanSpeed = 0
meanDirection = 0
day = str(datetime.today().day)
month = str(datetime.today().month)
hour = 0

if 10 <= int(L[0][5:7]) <= 12:
    hour = 10
elif 13 <= int(L[0][5:7]) <= 15:
    hour = 13
elif 16 <= int(L[0][5:7]) <= 18:
    hour = 16
elif 19 <= int(L[0][5:7]) <= 21:
    hour = 19
elif 22 <= int(L[0][5:7]):
    hour = 22

for i in range(len(L)):
    value = L[i].split(" ")
    print(value)

    meanSpeed += float(value[2])
    meanDirection += float(value[3])

print(meanSpeed / len(L))
print(meanDirection / len(L))

f = open("ppData.txt", "a", encoding='utf8')
f.writelines(str(day) + "-" + str(month) + " ")
f.writelines(str(hour) + " ")
f.writelines("%.1f" % (meanSpeed / len(L)) + " ")
f.writelines("%.0f" % (meanDirection / len(L)) + " ")
f.writelines("\n")
f.close()
