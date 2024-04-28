import numpy as np

f = open("dataMean.txt", "r", encoding='utf8')
dataReal = f.readlines()
f.close()

f = open("WindguruData.txt", "r", encoding='utf8')
dataPrediction = f.readlines()
f.close()


def findWindInfo(data):
    speed = []
    direction = []
    for line in range(len(data)):
        speed.append(float(data[line].split(" ")[2]))
        direction.append(float(data[line].split(" ")[3]))

    return speed, direction


def write_info():
    predictedSpeed, predictedDirection = findWindInfo(dataPrediction)
    realSpeed, realDirection = findWindInfo(dataReal)

    f = open("speed.txt", "w", encoding='utf8')

    for i in range(len(predictedSpeed)):
        f.writelines(str(predictedSpeed[i]) + " " + str(realSpeed[i]) + "\n")

    f.writelines("\n")
    f.close()

    f = open("direction.txt", "w", encoding='utf8')

    for i in range(len(predictedSpeed)):
        f.writelines(str(predictedDirection[i]) + " " + str(realDirection[i]) + "\n")

    f.writelines("\n")
    f.close()

write_info()