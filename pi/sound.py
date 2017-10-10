#content = UTF-8
import RPi.GPIO as GPIO
import time

LED = 15
SOUND = 14

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(SOUND, GPIO.IN)

ledOn = False

try:
	while True:
		on = GPIO.input(SOUND) == 1 if True else False
		if on :
			if ledOn == False :
				ledOn = True
				GPIO.output(LED, GPIO.HIGH)
			else:
				ledOn = False
				GPIO.output(LED, GPIO.LOW)
			time.sleep(0.1)				
			

except KeyboardInterrupt:
	GPIO.cleanup()
