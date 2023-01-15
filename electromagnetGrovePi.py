import time
from gpiozero import Button
##import grovepi
##
##electromagnet = 4
##
##grovepi.pinMode(electromagnet, "OUTPUT")
##time.sleep(1) #put the time we actually want the magnet turned on for
##
###sample code
##while True:
##    try:
##        #switches on the electromagnet
##        grovepi.digitalWrite(electromagnet, 1)
##        print("electromagnet is on")
##        time.sleep(2)
##
##        #switches off the electromagnet
##        grovepi.digitalWrite(electromagnet, 0)
##        print("electromagnet is off")
##        time.sleep(2)
##
##    except KeyboardInterrupt:
##        grovepi.digitalWrite(electromagnet, 0)
##        break
##    except IOError:
##        print("Error")
##
###code that makes sense for our product
##

##pushButton = Button(26)
##counter = 0
##while True:
##    time.sleep(0.5)
##    if pushButton.is_pressed:
##        counter += 1
##        print("button was pressed", counter, "times")
##    else:
##        print("button is not pressed")

def deviceOnOff(lowStandard, pushButton, sensorData, leftDiff):
    time.sleep(0.3)
    if pushButton.is_pressed == True:
        print("Patient is wearing the device!")
        time.sleep(0.3)
##        if :
##            print("Kevin is unbalanced ", leftDiff, "degrees")
##            counter += 1
##            time.sleep(1)
    else:
        print("Kevin is not wearing the device. Kevin, please put on the device")
        

