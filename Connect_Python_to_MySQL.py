import MySQLdb

conn = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
cursor = conn.cursor()
cursor.execute('SELECT COUNT(UserID) as count FROM User WHERE id = 1')
row = cursor.fetchone()
conn.close()
print(row)
