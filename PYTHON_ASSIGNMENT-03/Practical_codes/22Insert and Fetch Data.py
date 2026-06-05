import sqlite3

con = sqlite3.connect("student.db")
cur = con.cursor()

cur.execute("INSERT INTO student VALUES(1,'Alice')")
con.commit()

cur.execute("SELECT * FROM student")
print(cur.fetchall())

con.close()