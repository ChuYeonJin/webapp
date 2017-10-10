import MySQLdb

db = MySQLdb.connect('movingtalk.kro.kr', 'movingtalk', 'chu1', 'testdb')
cur = db.cursor()
sql = "insert into clients value ('2', 'chu2', '010')"

try:
    cur.execute(sql)
    db.commit()
    print ('성공')
except all as t:
    db.rollback()
    print ('실패 :',t)

cur.close()
db.close()