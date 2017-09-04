
from flask import Flask, request
import RPi.GPIO as GPIO

app = Flask(__name__) #make instance

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)

@app.route('/')
def index():
	return 'This is the Homepage'

@app.route('/profile/<username>')
def profile(username):
	return 'Hey there %s' %username

@app.route('/post/<int:post_id>')
def post(post_id):
	return '<h2>Post ID is %d</h2>' %post_id

@app.route('/led/<led>')
def led(led):
	if led == "on":
		GPIO.output(15, GPIO.HIGH)
		return "LED ON"
	elif led == "off":
		GPIO.output(15, GPIO.LOW)
		return "LED OFF"
	else:
		return "?"

if __name__ == "__main__":
	try:
		app.run(debug=True, host='0.0.0.0', port=9209)
	except Keyboardinterrupt:
		GPIO.cleanup()
