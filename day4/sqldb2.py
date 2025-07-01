import sqlite3
conn = sqlite3.connect("db1.db")

conn.execute("delete from server where user_id={id}")
conn.commit()
data=conn.execute("selct*user1")
for x in data:print(x)
conn.close()