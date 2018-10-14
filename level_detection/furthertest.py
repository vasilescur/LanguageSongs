import sqlite3

conn = sqlite3.connect('pembis.db')
 conn.execute('CREATE TABLE numbers (id)')
cur = conn.cursor()
numbers = [1,2,3,4,5,6,7]
for number in numbers:
 cur.execute('INSERT INTO numbers ')
