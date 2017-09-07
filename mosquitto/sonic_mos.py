import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
LED = 15
GPIO_TRIGGER = 24
GPIO_ECHO = 23

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def on_connect(client, userdata, flags, rc):
    print("Con : " + str(rc))
    client.subscribe("test")

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

broker = "192.168.0.126"
port = 1883

# mqtt setting
client = mqtt.Client()
client.connect(broker, port)

led_state = "LEDOFF"

try:
    while True:
        dist = distance()
        global led_state

        if dist <= 10:
            if led_state == "LEDOFF":
                client.publish("test", "LEDON")
                led_state = "LEDON"

        elif dist > 3000:
            continue
        else:
            if led_state == "LEDON":
                client.publish("test", "LEDOFF")
                led_state = "LEDOFF"

        time.sleep(1)

except KeyboardInterrupt :
    GPIO.cleanup()