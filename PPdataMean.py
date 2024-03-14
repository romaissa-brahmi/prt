import numpy as np
import math

hour_4 = []
hour_7 = []
hour_10 = []
hour_13 = []
hour_16 = []
hour_19 = []
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

    if 4 <= hour <= 6:
        hour_4.append([day, hour, speed, direction])

    elif 7 <= hour <= 9:
        hour_7.append([day, hour, speed, direction])

    elif 10 <= hour <= 12:
        hour_10.append([day, hour, speed, direction])

    elif 13 <= hour <= 15:
        hour_13.append([day, hour, speed, direction])

    elif 16 <= hour <= 18:
        hour_16.append([day, hour, speed, direction])

    elif 19 <= hour <= 21:
        hour_19.append([day, hour, speed, direction])

    elif 22 <= hour <= 23:
        hour_22.append([day, hour, speed, direction])


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

    return str(hour[0][0]) + " " + str(hour[0][1]) + " " + str(round(mean_speed, 1)) + " " + str(mean_dir) + "\n"


def write_info():

    f = open("/home/ubuntu/prt/PPdataMean.txt", "a", encoding='utf8')

    f.writelines(write_line(hour_4))
    f.writelines(write_line(hour_7))
    f.writelines(write_line(hour_10))
    f.writelines(write_line(hour_13))
    f.writelines(write_line(hour_16))
    f.writelines(write_line(hour_19))
    f.writelines(write_line(hour_22))

    f.writelines("\n")

    f.close()


f = open("/home/ubuntu/prt/PacificPalissadesData.txt", "r", encoding='utf8')
data = f.readlines()
f.close()

divide_values_by_hours(data)
write_info()

