from datetime import datetime

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
