from flask import Flask, render_template
import MySQLdb

app = Flask(__name__)

@app.route('/')
def index():
    db = MySQLdb.connect('movingtalk.kro.kr', 'movingtalk', 'chu1', 'testdb')
    cur = db.cursor()
    sql = "select * from clients"
    cur.execute(sql)
    rs = cur.fetchall()
    templateData = {'data' : rs}
    cur.close()
    db.close()
    return render_template('mysql_flask.html', **templateData)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9209)