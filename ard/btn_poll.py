import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN)

cnt = 0

while True:
    value = GPIO.input(18)
    if value == True:
        count = count + 1
        print (cnt)

    time.sleep(0.1)

