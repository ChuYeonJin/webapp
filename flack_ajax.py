import RPi.GPIO as GPIO
from flask import Flask, request, jsonify, render_template
import time

app = Flask(__name__)

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
LED = 15
GPIO_TRIGGER = 24
GPIO_ECHO = 23

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

from sonic import distance

@app.route("/")
def index():
    return render_template('sonic.html')

@app.route("/ajax")
def ajax():
    result = distance()
    return jsonify(result = result)

if __name__ == "__main__":
	try:
		 app.run(host='192.168.0.126', port=9209, debug=True)

	except KeyboardInterrupt:
		GPIO.cleanup()
