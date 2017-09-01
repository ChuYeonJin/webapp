import RPi.GPIO as GPIO
import time
from flask import Flask, request

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

LED1 = 15

GPIO.setup(LED1, GPIO.OUT, initial=GPIO.LOW)

@app.route("/")
def hello():
    return "Flask Test"

@app.route("/led", methods=['GET'])
def led():
    temp = request.args.get('led')
    if temp == "on":
        GPIO.output(LED1, GPIO.HIGH)
        return "LED ON"
    else:
        if temp == "off":
            GPIO.output(LED1, GPIO.LOW)
            return "LED OFF"

if __name__ == "__main__":
	try:
		 app.run(host='192.168.0.126', port=9209, debug=True)

	except KeyboardInterrupt:
		GPIO.cleanup()
