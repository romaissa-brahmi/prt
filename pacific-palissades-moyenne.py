from datetime import datetime

L = []

f = open("ppRawData.txt", "r", encoding='utf8')
L = f.readlines()
f.close

for i in range (len(L)):






    ff



f = open("ppRawData.txt", "a", encoding='utf8')
f.writelines(str(datetime.today().day) + "-" + str(datetime.today().month) + " ")
f.writelines(str(datetime.today().hour) + " ")
f.writelines(windSpeed + " ")
f.writelines(windDirection + " ")
f.writelines("\n")
f.close
