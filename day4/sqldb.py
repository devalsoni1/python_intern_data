import sqlite3
conn = sqlite3.connect("db1.db")

conn.execute('''
create table user(
userid INTEGER PRIMARY KEY AUTOINCREMENT,
usernm VARCHAR (100),
pass VARCHAR (100)
)
''')

conn.close()