import gpiozero
import time 
from sensor_library import *
from gpiozero import Button

### standard = int(input("Enter the standard orientation"))
### highStandard = standard + 10
### lowStandard = standard - 10
### sensorData = "PUT A VALUE IN HERE"
### 
### rightDiff = sensorData - highStandard
### leftDiff = sensorData - lowStandard
sensorData=11
standard = 3
highStandard = standard + 2
lowStandard = standard - 2
rightDiff = sensorData - 2
leftDiff = sensorData - 2
pushButton = Button(26)
def deviceOnOff(standard, highStandard, lowStandard, pushButton, sensorData):

    while True:
        counter = 0
        print("Kevin is not wearing the device. Kevin, please put on the device")
        time.sleep(0.3)
        if pushButton.is_pressed == True:
            counter += 1
            while counter <=1:
                print("Patient is wearing the device!")
                time.sleep(0.3)
                if sensorData >= highStandard:
                    print("Kevin is unbalanced ",rightDiff, "degrees")
                elif sensorData < lowStandard:
                    print("Kevin is unbalanced ", leftDiff, "degrees")
                time.sleep(0.3)






##    while True:
####        push_button = False #make sure boolean operator is correct
##        pushButtonState = False
##        if pushButton.is_pressed == True:
##            print("Patient is wearing the device! ") #put name of device here 
##            pushButtonState = True
##            while pushButtonState == True:
##                if sensorData > highStandard:
##                    print(("Kevin is unbalanced ", rightDiff, "degrees"))
##                elif sensorData < lowStandard:
##                    print("Kevin is unbalanced by ", leftDiff, "degrees")
##        elif pushButton.is_pressed != True:
##            print("Kevin is not wearing the device. Kevin, please put on the device")
##
                
##        if pushButton.is_pressed === True:
##            pushButtonState = 1
##        elif pushButton.is_pressed == True:
##            pushButtonState = 2
##        if pushButtonState == 1:
##            print("Patient is wearing the device!")
##            if sensorData >= highStandard:
##                print("Kevin is unbalanced ",rightDiff, "degrees"))
##            elif sensorData < lowStandard:
##                print("Kevin is unbalanced by ",leftDiff, "degrees")
##        elif pushButtonState == 2        
            
##        else:
##            print("Kevin is not wearing the device. Kevin, please put on the device " ) #put name of device here
##



##x = 10
##y = 11
##z = x-y
##zz = x+y
##pushButton = Button(26)
##counter = 0
##while True:
##    if pushButton.is_pressed == True:
##        counter +=1
##        print("button is pressed", counter, "times")





















##
##
##    for counter in range(10, 0, -1): 
##        if have_seizure: #have_Seizure is initialized in main() as a boolean
##            print("Press the button if you would like to temporarily stop the program")
##            print(counter)
##        time.sleep(1)
##        if push_button.is_pressed:
##            print("Patient is not having a seizure. False alarm")
##            print("Buzzer is off","\n","LEDs are off","\n")
##            time.sleep(30) #proof of concept. Would normally be time.sleep(1200) but for sake of presentation --> 30 seconds 
##            have_seizure=False
##            buzzer_object.off()
##            led1.off()
##            led2.off()
##            led3.off()
##            return have_seizure      
##    if have_seizure: #have_seizure is True in main()
##        
##        print("Patient is having a seizure. Call 911")
##        buzzer_object.on()
##        led1.on()
##        led2.on()
##        led3.on()
##        print("Buzzer is on","\n","LEDs are on","n")
##
