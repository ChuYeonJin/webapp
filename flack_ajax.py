from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

from sonic import distance

@app.route("/")
def index():
    return render_template('sonic.html')

@app.route("/ajax")
def ajax():
    result = distance()
    print result
    return jsonify(result = result)

if __name__ == "__main__":
	try:
		 app.run(host='192.168.0.126', port=9209, debug=True)

	except KeyboardInterrupt:
		GPIO.cleanup()
