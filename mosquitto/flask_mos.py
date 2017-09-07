from flask import Flask, render_template
import paho.mqtt.client as mqtt

app = Flask(__name__) #make instance

broker = "192.168.0.126"
port = 1883

# mqtt setting
client = mqtt.Client()
client.connect(broker, port)

@app.route("/")
def index():
    return render_template('ledCon.html')

@app.route("LED/ON")
def led_on():
	client.publish("test", "LEDON")
	return "LED ON"

@app.route("LED/OFF")
def led_off():
	client.publish("test", "LEDOFF")
	return "LED OFF"

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=9209)
