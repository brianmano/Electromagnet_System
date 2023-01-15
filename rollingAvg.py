from sensor_library import *
import time
import gpiozero
from gpiozero import Button, LED
import grovepi

sensor = Orientation_Sensor()
dataList = []
def inputData(sensor, dataList):
    allAngles= sensor.euler_angles()
##    print(allAngles)
##    print(allAngles[1])
##    type(allAngles)
    Angle = int(allAngles[1])
##    print("Euler angle Z:", allAngles[1])
    time.sleep(0.4)
    if len(dataList) > 10:
        del dataList[0]
    dataList.append(Angle)
##    print("The list of data is", dataList)
    return Angle, dataList
def calculateRollingAvg(dataList):
    sensorData = sum(dataList) /len(dataList)
##    print("The rolling average is", sensorData)
    return sensorData
def diff(standard, sensorData):
    highStandard = standard + 10
    rightDiff = sensorData + 10
##    print("The low standard is", lowStandard)
##    print("The left difference is", leftDiff)
    return highStandard, rightDiff

def deviceOnOff(highStandard, pushButton, sensorData, rightDiff):
    time.sleep(0.3)
    if pushButton.is_pressed == True:
        print("Patient is wearing the device!")
        time.sleep(0.3)
##        print(leftDiff)
        if sensorData > highStandard:
            print("Kevin is unbalanced ", round(rightDiff, 2), "degrees")
            time.sleep(1)
    else:
        print("Kevin is not wearing the device. Kevin, please put on the device")


def ledArray(led1, led2, led3, led4, led5, pushButton, sensorData, highStandard):
    if pushButton.is_pressed == True:
            if sensorData > highStandard:
                led1.on()
                led2.on()
                led3.on()
                led4.on()
                led5.on()
                print("led1 is on")
                print("led2 is on")
                print("led3 is on")
                print("led4 is on")
                print("led5 is on")

                time.sleep(0.3)
                led1.off()
                print("led1 is off")
                led2.off()
                print("led2 is off")
            
                time.sleep(0.3)
                led3.off()
                print("led3 is on")
                led4.off()
                print("led4 is off")
            
                time.sleep(0.3)
                led5.off()
                print("led5 is off")

            else:
                led1.off()
                led2.off()
                led3.off()
                led4.off()
                led5.off()
                print("all leds are off")

##            time.sleep(0.3)

electromagnet = 4
# x = 12
grovepi.pinMode(electromagnet, "OUTPUT")
def electromagnet(electromagnet, highStandard, pushButton, sensorData):
    if pushButton.is_pressed == True:
        if sensorData > highStandard:
            try:
                #switches on the electromagnet
                grovepi.digitalWrite(electromagnet, 1)
                print("electromagnet is on. Kevin is unbalanced.")
                time.sleep(0.5) #switch to time we actually want
##
##                #switches off the electromagnet
##                grovepi.digitalWrite(electromagnet, 0)
##                print("electromagnet is off. Kevin is balanced")
##                time.sleep(0.5) #switch to time we actually want

            except KeyboardInterrupt:
                grovepi.digitalWrite(electromagnet, 0)
                # break
            except IOError:
                print("Error")
            
        else:
            grovepi.digitalWrite(electromagnet, 0)
            print("electromagnet is off. Kevin is balanced. ")
            time.sleep(2) #play around with this variable!!!
##            
def main():
    standard = -90
    pushButton = Button(26)
    led1 = LED(10)
    led2 = LED(22)
    led3 = LED(9)
    led4 = LED(11)
    led5 = LED(0)

    while True:
        inputData(sensor, dataList)
        sensorData = calculateRollingAvg(dataList)
        highStandard = diff(standard, sensorData)[0]
##        leftDiffTup = diff(standard, sensorData)
        rightDiff = diff(standard, sensorData)[1]
##        print(rightDiff)
        deviceOnOff(highStandard, pushButton, sensorData, rightDiff)
##        electromagnet(electromagnet, leftDiff)
        electromagnet(electromagnet, highStandard, pushButton, sensorData)
        ledArray(led1, led2, led3, led4, led5, pushButton, sensorData, highStandard)
