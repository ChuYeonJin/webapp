import RPi.GPIO as GPIO
import time
import request
from flask import Flask
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

LED1 = 23
LED2 = 25

GPIO.setup(LED1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED2, GPIO.OUT, initial=GPIO.LOW)

@app.route("/")
def hello():
    return "Flask Test"

@app.route("/led")
def led():
    GPIO.output(LED1, GPIO.HIGH)
    return "LED ON"

if __name__ == "__main__":
    app.run(host='192.168.0.126', port=8889, debug=True)
