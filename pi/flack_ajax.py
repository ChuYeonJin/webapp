from flask import Flask, request, jsonify, render_template

import sonic

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('sonic.html')

@app.route("/ajax")
def ajax():
    result = sonic.distance()
    return jsonify(result=result)

if __name__ == "__main__":
	try:
		 app.run(host='192.168.0.126', port=9209, debug=True)

	except KeyboardInterrupt:
		sonic.GPIO.cleanup()
