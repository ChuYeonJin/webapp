#Libraries
import RPi.GPIO as GPIO
import time
import os

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 24
GPIO_ECHO = 23
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

#global
LED = False
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    distance = round(distance, 2)
 
    return distance

def turnLED(dist, condition):
    dist = distance()
    global LED
    if dist <= condition:
	if LED == False:
		os.system("curl http://192.168.0.126:9209/led/on")
		LED = True
    else:
	if  LED :
		os.system("curl http://192.168.0.126:9209/led/off")
		LED = False


if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            turnLED(dist, 20)
                
            print "dist : ", dist
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print "Measurement stopped by User"
        GPIO.cleanup()
