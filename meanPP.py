from datetime import datetime, timedelta

import numpy as np
import math

hour_5 = []
hour_8 = []
hour_11 = []
hour_14 = []
hour_17 = []
hour_20 = []
hour_22 = []


def get_coords(data):
    list_angle = []
    for line in data:
        list_angle.append(line[3])

    list_angle_radians = np.deg2rad(list_angle)

    coords = []
    for i in range(len(list_angle_radians)):
        coords.append([np.cos(list_angle_radians[i]), np.sin(list_angle_radians[i])])

    return np.array(coords)


def mean_coords(coords):
    mean_cos = np.mean(coords[:, 0])
    mean_sin = np.mean(coords[:, 1])
    norm = np.sqrt(mean_cos ** 2 + mean_sin ** 2)

    return mean_cos / norm, mean_sin / norm


def find_angle(coords):
    cos_value, sin_value = mean_coords(coords)

    angle = math.degrees(math.atan2(sin_value, cos_value))
    angle = angle % 360
    return round(angle, 1)


def switch_function(day, hour, speed, direction):

    if 5 <= hour <= 7:
        hour_5.append([day, hour, speed, direction])

    elif 8 <= hour <= 10:
        hour_8.append([day, hour, speed, direction])

    elif 11 <= hour <= 13:
        hour_11.append([day, hour, speed, direction])

    elif 14 <= hour <= 16:
        hour_14.append([day, hour, speed, direction])

    elif 17 <= hour <= 19:
        hour_17.append([day, hour, speed, direction])

    elif 20 <= hour <= 23:
        hour_20.append([day, hour, speed, direction])


def divide_values_by_hours(data):

    for line in range(len(data)):
        day = data[line].split(" ")[0]
        hour = int(data[line].split(" ")[1])
        speed = float(data[line].split(" ")[2])
        direction = float(data[line].split(" ")[3])

        switch_function(day, hour, speed, direction)


def mean_wind_speed(data):
    list = []
    for line in data:
        list.append(line[2])
    return np.mean(np.array(list))


def write_line(hour):
    mean_speed = mean_wind_speed(hour)
    mean_dir = find_angle(get_coords(hour))

    day = str(hour[0][0])
    if len(day) == 1:
        day = "0" + day

    time = str(hour[0][1])
    if len(time) == 1:
        time = "0" + time


    return str(day + " " + time + " " + str(round(mean_speed, 1)) + " " + str(mean_dir) + "\n")


def write_info():

    f = open("/home/ubuntu/prt/dataMean.txt", "a", encoding='utf8')

    f.writelines(write_line(hour_5))
    f.writelines(write_line(hour_8))
    f.writelines(write_line(hour_11))
    f.writelines(write_line(hour_14))
    f.writelines(write_line(hour_17))
    f.writelines(write_line(hour_20))
    f.writelines(write_line(hour_22))

    f.writelines("\n")
    f.writelines("\n")


    f.close()


yesterday = str((datetime.today() - timedelta(1)).day)
if len(yesterday) == 1:
    today = "0" + yesterday


f = open("/home/ubuntu/prt/PacificPalissades.txt", "r", encoding='utf8')
data = f.readlines()
f.close()

divide_values_by_hours(data)
write_info()

