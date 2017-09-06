import MySQLdb

db = MySQLdb.connect('movingtalk.kro.kr', 'movingtalk', 'chu1', 'testdb')
cur = db.cursor()
sql = "SELECT * FROM clients"
cur.execute(sql)
rs = cur.fetchall()

result = []

for item in rs:
    result.append(list(item))

for item2 in result:
    print('id : ' + str(item2[0]), 'name : ' + str(item2[1]), 'phone : ' + str(item2[2]))

cur.close()
db.close()