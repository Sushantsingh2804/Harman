import sqlite3

conn = sqlite3.connect("College.db")

getRollno = input("Enter the Roll no- ")

cursor = conn.execute("SELECT * FROM STUDENT WHERE ROLLNO="+getRollno)


for i in cursor:
    print("id-", i[0])
    print("Name-", i[1])
    print("Roll Numbers-", i[2])
    print("Admission Number-", i[3])
    print("College-", i[4])
    print("------------------------------------------------------")