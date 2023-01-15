import time 
import grovepi

electromagnet = 4
x = 12

grovepi.pinMode(electromagnet, "OUTPUT")
##time.sleep(1) #put the time we actually want the magnet turned on for

#sample code
def electromagnet(x, electromagnet):
    while True:
        if x > 11: 
            try:
                #switches on the electromagnet
                grovepi.digitalWrite(electromagnet, 1)
                print("electromagnet is on")
                time.sleep(2) #switch to time we actually want

                #switches off the electromagnet
                grovepi.digitalWrite(electromagnet, 0)
                print("electromagnet is off")
                time.sleep(2) #switch to time we actually want

            except KeyboardInterrupt:
                grovepi.digitalWrite(electromagnet, 0)
                break
            except IOError:
                print("Error")
                
        else:
            grovepi.digitalWrite(electromagnet, 0)
            print("electromagnet is off")
            time.sleep(5)
