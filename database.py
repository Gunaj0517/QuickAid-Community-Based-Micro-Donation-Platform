import sqlite3 as sq3
con=sq3.Connection('database.db')
cur=con.cursor()

cur.execute('Select * from requests')
fileData=cur.fetchall()
for i in fileData:
    print(i)