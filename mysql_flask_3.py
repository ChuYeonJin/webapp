from flask import Flask, render_template
import MySQLdb

app = Flask(__name__)

def createDB():
    db = MySQLdb.connect('movingtalk.kro.kr', 'movingtalk', 'chu1', 'testdb')
    cur = db.cursor()
    return db, cur

def closeDB(db, cur):
    cur.close()
    db.close()

@app.route('/')
def index():
    db,cur = createDB()
    sql = "select * from clients"
    cur.execute(sql)
    rs = cur.fetchall()
    templateData = {'data' : rs}
    closeDB(db,cur)
    return render_template('mysql_flask.html', **templateData)

@app.route('/GET/ID/<string:id>')
def get_id(id):
    db, cur = createDB()
    sql = "select * from clients where cli_name= '%s'" % id
    cur.execute(sql)
    rs = cur.fetchall()
    closeDB(db, cur)
    return (render_template('select_id.html', data = rs))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9209)