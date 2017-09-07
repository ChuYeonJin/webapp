#Libraries
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)

def on_connect(client, userdata, flags, rc):
    print("Con : " + str(rc))
    client.subscribe("test")

def on_message(client, userdata, msg):
    strMsg = str(msg.payload)
    print(msg.topic + " : " + strMsg)
    if(strMsg == "LEDON"):
        GPIO.output(10, GPIO.HIGH)
    elif(strMsg == "LEDOFF"):
        GPIO.output(10, GPIO.LOW)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.0.126", 1883, 60)
client.loop_forever()
