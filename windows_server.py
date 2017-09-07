from flask import Flask, render_template, request
import MySQLdb

app = Flask(__name__)

def createDB():
    db = MySQLdb.connect('movingtalk.kro.kr', 'movingtalk', 'chu1', 'testdb')
    cur = db.cursor()
    return db, cur

def closeDB(db, cur):
    cur.close()
    db.close()

def cud(sql):
    db, cur = createDB()

    try:
        rs = cur.execute(sql)
        db.commit()
        closeDB(db, cur)
        if rs == 0:
            return 0
        return 1

    except:
        db.rollback()
        closeDB(db, cur)
        return 0

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/GET')
def select():
    db,cur = createDB()
    sql = "select * from clients"
    cur.execute(sql)
    rs = cur.fetchall()
    templateData = {'data' : rs}
    closeDB(db,cur)
    return render_template('mysql_flask.html', **templateData)

@app.route('/GET/<string:id>')
def get_id(id):
    db, cur = createDB()
    sql = "select * from clients where cli_name= '%s'" % id
    cur.execute(sql)
    rs = cur.fetchall()
    closeDB(db, cur)
    return (render_template('select_id.html', data = rs))

@app.route('/POST', methods=['GET', 'POST'])
@app.route('/PUT', methods=['GET', 'POST'])
@app.route('/DELETE', methods=['GET', 'POST'])
def cud_case():
    url = request.url.split("9209/")[1]
    if request.method == 'GET':
        return (render_template('cud.html', url = url))

    name = request.form['name']
    tel = request.form['tel']
    switch = {
        'POST' : "INSERT INTO `testdb`.`clients` (`cli_name`, `cli_tel`) VALUES ('"+ name +"', '"+ tel +"')",
        'PUT' : "UPDATE clients SET cli_tel='"+ tel +"' where cli_name = '"+ name +"'",
        'DELETE' : "DELETE FROM clients WHERE cli_name = '"+ name +"' AND cli_tel = '"+ tel +"'"
    }

    sql = switch[url]

    result = cud(sql)

    if result == 0:
        return "실패"
    else:
        return "성공"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9209)