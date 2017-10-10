from flask import Flask, request, render_template

app = Flask(__name__) #make instance

@app.route('/')
def index():
    return 'Method used: %s' %request.method

@app.route('/profile/<name>')
def profile(name):
    return render_template('profile.html', key = name)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9209)