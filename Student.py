import sqlite3

conn = sqlite3.connect("College.db")

conn.execute(''' CREATE TABLE IF NOT EXISTS STUDENT(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NAME TEXT,
                ROLLNO INTEGER,
                ADMNO INTEGER,
                COLLAGE TEXT
);''')

print(" Table Creation Successful ")

getName = input("Enter the Name- ")
getRollNumber = input("Enter Roll Number- ")
getAdmno = input("Enter Admission Number- ")
getCollege = input("Enter Collage Name- ")

conn.execute("INSERT INTO STUDENT(NAME,ROLLNO,ADMNO,COLLAGE) VALUES ('"+getName+"',"+getRollNumber+","+getAdmno+",'"+getCollege+"')")
print("Table created successfully")
conn.commit()
conn.close()
