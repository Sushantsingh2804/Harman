import sqlite3

conn = sqlite3.connect("College.db")

cursor = conn.execute("SELECT * FROM STUDENT")

for i in cursor:
    print("id-", i[0])
    print("Name-", i[1])
    print("Roll Numbers-", i[2])
    print("Admission Number-", i[3])
    print("College-", i[4])
    print("------------------------------------------------------")
