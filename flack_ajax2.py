# coding:utf-8
from flask import Flask, request, jsonify, render_template
import time

app = Flask(__name__)

from sonic import distance

@app.route("/")
def index():
    return render_template('sonic2.html')

@app.route("/ajax")
def ajax():
    result = distance()
    return jsonify(result=result, curr_time=u(time.strftime("%Y년 %m월 %d일 / %H : %M")))

if __name__ == "__main__":
	try:
		 app.run(host='192.168.0.126', port=9209, debug=True)

	except KeyboardInterrupt:
		GPIO.cleanup()
