import gpiozero
import time 
from gpiozero import LED
from gpiozero import Button
##from sensor_library import *

##standard = int(input("Enter the standard orientation"))
##highStandard = standard + 10
##lowStandard = standard - 10
##sensorData = "PUT A VALUE IN HERE"


##push_button = Button(26)

x = 11
led1 = LED(10)
led2 = LED(22)
led3 = LED(9)
led4 = LED(11)
led5 = LED(0)
pushButton = Button(26)
##push = False
#def ledArray(push_button, led1, led2, led3, led4led5, sensorData, highStandard, lowStandard):
def ledArray(x, led1, led2, led3, led4, led5, pushButton):
   while True:
##      while push == True:
      if pushButton.is_pressed:
            print("")
                 #if sensorData > highStandard or sensorData < lowStandard: #do we really need high standard and low standard? or just one?
            if x>3:
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


