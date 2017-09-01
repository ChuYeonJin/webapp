from flask import Flask, request

app = Flask(__name__) #make instance

@app.route('/')
def index():
	return 'This is the Homepage'

@app.route('/test')
def test():
	return 'test'

@app.route('/tuna')
def tuna():
	return '<h2>Tuna is Good</h2>'

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=9209)
