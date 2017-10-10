from flask import Flask, request

app = Flask(__name__) #make instance

@app.route('/')
def index():
	return 'This is the Homepage'

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=9209)
