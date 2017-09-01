import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

def reset():
	for i in range(1, 41):
		GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)
		GPIO.output(8, GPIO.LOW)
	print "reset"

except KeyboardInterrupt:
	pass
reset()
GPIO.cleanup()
