import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
cnt = 0
def handler(channel):
    count = cnt + 1
    print(cnt)

GPIO.setup(18, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(18, GPIO.RISING, callback=handler)

while True:
    time.sleep(1)