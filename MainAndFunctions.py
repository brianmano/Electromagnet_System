import gpiozero
import time
import grovepi
from sensor_library import *
from gpiozero import Button, LED

# sensor = Orientation_Sensor()
# dataList = []
#has a while True
def inputData(sensor, dataList):
    allAngles= sensor.euler_angles()
    zAngle = allAngles[2]
    print("Euler angle Z:", allAngles[2])
    time.sleep(0.4)
    if len(dataList) > 10:
        del dataList[0]
    dataList.append(zAngle)
##        print("The list of data is", dataList)
    return zAngle, dataList

def calcRollingAvg(dataList):
##    sensorData = sum(dataList) /len(dataList)
##    return sensorData
    sensorData = sum(dataList) /len(dataList)
    print("The rolling average is", sensorData)
    return sensorData

def diff(standard, sensorData):
    lowStandard = standard - 2
    leftDiff = sensorData - 2
    print("The low standard is", lowStandard)
    print("The left difference is", leftDiff)
    return lowStandard, leftDiff



#has a while True
def deviceOnOff(lowStandard, pushButton, sensorData, leftDiff):
    counter = 0
    print("Kevin is not wearing the device. Kevin, please put on the device")
    time.sleep(0.3)
    if pushButton.is_pressed == True:
        counter += 1
        while counter <=1:
            print("Patient is wearing the device!")
            time.sleep(0.3)
            # if sensorData >= highStandard:
            #     print("Kevin is unbalanced ",rightDiff, "degrees") #probably won't need since only right side is bad 
            if sensorData < lowStandard:
                print("Kevin is unbalanced ", leftDiff, "degrees")
            time.sleep(0.3)


electromagnet = 4
# x = 12
grovepi.pinMode(electromagnet, "OUTPUT")
##time.sleep(1) #put the time we actually want the magnet turned on for
#Has a while True
def electromagnet(sensorData, electromagnet, lowStandard):
    if sensorData < lowStandard: 
        try:
            #switches on the electromagnet
            grovepi.digitalWrite(electromagnet, 1)
            print("electromagnet is on. Kevin is unbalanced.")
            time.sleep(0.5) #switch to time we actually want

            #switches off the electromagnet
            grovepi.digitalWrite(electromagnet, 0)
            print("electromagnet is off. Kevin is balanced")
            time.sleep(0.5) #switch to time we actually want

        except KeyboardInterrupt:
            grovepi.digitalWrite(electromagnet, 0)
            # break
        except IOError:
            print("Error")
            
    else:
        grovepi.digitalWrite(electromagnet, 0)
        print("electromagnet is off")
        time.sleep(5)

def ledArray(led1, led2, led3, led4, led5, pushButton, sensorData, lowStandard):
##      
# while push == True:
    counter = 0
    if pushButton.is_pressed == True:
        counter += 1
        while counter <=1:
            if sensorData < lowStandard:
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

                time.sleep(1)
                led1.off()
                print("led1 is off")
                led2.off()
                print("led2 is off")
            
                time.sleep(1)
                led3.off()
                print("led3 is on")
                led4.off()
                print("led4 is off")
            
                time.sleep(1)
                led5.off()
                print("led5 is off")

            else:
                led1.off()
                led2.off()
                led3.off()
                led4.off()
                led5.off()
                print("all leds are off")

            time.sleep(0.3)

def main():
    sensor = Orientation_Sensor()
    dataList = []
##    sensorData=11
    standard = 3
    # highStandard = standard + 2
##    lowStandard = standard - 2
    # rightDiff = sensorData - 2
##    leftDiff = sensorData - 2
    pushButton = Button(26)
    electromagnet = 4
    led1 = LED(10)
    led2 = LED(22)
    led3 = LED(9)
    led4 = LED(11)
    led5 = LED(0)

    while True:
        inputData(sensor, dataList)
        sensorData = calcRollingAvg(dataList)
        lowStandard = diff(standard, sensorData)
        leftDiff = diff(standard, sensorData)
        deviceOnOff(lowStandard, pushButton, sensorData, leftDiff)
        electromagnet(sensorData, electromagnet)
        ledArray(led1, led2, led3, led4, led5, pushButton, sensorData, lowStandard)
