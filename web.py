import RPi.GPIO as GPIO
import time
from flask import Flask, request
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
    temp = request.form["led"]
    if temp == "on":
        GPIO.output(LED1, GPIO.HIGH)
        return "LED ON"
    else:
        if temp == "off":
            GPIO.output(LED1, GPIO.HIGH)
            return "LED OFF"

if __name__ == "__main__":
    app.run(host='192.168.0.126', port=8889, debug=True)
