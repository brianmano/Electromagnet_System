from sensor_library import *
import time

# sensor = Orientation_Sensor()
# 
# def testing(sensor):
#     while True:
#         all_angles = sensor.euler_angles()
#         print("Euler angle:", all_angles)
#         print("Euler angle X:", all_angles[0])
#         print("Euler angle Y:", all_angles[1])
#         print("Euler angle Z:", all_angles[2])
#         time.sleep(5)


##def inputData(sensor, allAngles, zAngle, dataList):
sensor = Orientation_Sensor()
dataList = []
def inputData(sensor, dataList):
    while True:
        all_angles= sensor.euler_angles()
        zAngle = all_angles[2]
        print("Euler angle Z:", all_angles[2])
        time.sleep(0.4)
        if len(dataList) > 10:
            del dataList[0]
        dataList.append(zAngle)
##        print("The list of data is", dataList)
    return zAngle, dataList

