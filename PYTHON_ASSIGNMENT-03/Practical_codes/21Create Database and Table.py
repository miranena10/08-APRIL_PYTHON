import sqlite3

con = sqlite3.connect("student.db")
cur = con.cursor()

cur.execute("CREATE TABLE student(id INTEGER, name TEXT)")

con.commit()
con.close()

print("Table created successfully")