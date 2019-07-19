from math import *

#计算两个经纬度之间的距离(python算法)

EARTH_REDIUS = 6378.137

def rad(d):
    return d * pi / 180.0

def getDistance(lat1, lng1, lat2, lng2):
    radLat1 = rad(lat1)
    radLat2 = rad(lat2)
    a = radLat1 - radLat2
    b = rad(lng1) - rad(lng2)
    s = 2 * sin(sqrt(pow(sin(a / 2), 2) + cos(radLat1) * cos(radLat2) * pow(sin(b / 2), 2)))
    s = s * EARTH_REDIUS
    return s

print(getDistance(37.571111,112.154167,37.581111,112.164167))

#print(geopy.distance.geodesic((37.571111,112.154167), (37.581111,112.164167)).m) #计算两个坐标直线距离
#print(geopy.distance.geodesic((37.571111,112.154167), (37.581111,112.164167)).km) #计算两个坐标直线距离