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
while True:
    print("Select option from menu: ")
    print("1. Add Student")
    print("2. Search an Student")
    print("3. Update an Student")
    print("4. Delete an Student")
    print("5. Exit")

    choice = int(input("Enter a choice:- "))
    if choice == 1:
        print("Selected an Option to add an Student\'s data")
        getName = input("Enter the Name- ")
        getRollNumber = input("Enter Roll Number- ")
        getAdmno = input("Enter Admission Number- ")
        getCollege = input("Enter Collage Name- ")
        conn.execute("INSERT INTO STUDENT(NAME,ROLLNO,ADMNO,COLLAGE) VALUES ('" + getName + "'," + getRollNumber + "," + getAdmno + ",'" + getCollege + "')")
        print("Record created successfully")
        conn.commit()

    elif choice == 2:
        print("Selected an Option to search an Student\'s data")
        getRollno = input("Enter the Roll no- ")
        cursor = conn.execute("SELECT * FROM STUDENT WHERE ROLLNO=" + getRollno)
        for i in cursor:
            print("id-", i[0])
            print("Name-", i[1])
            print("Roll Numbers-", i[2])
            print("Admission Number-", i[3])
            print("College-", i[4])
            print("------------------------------------------------------")

    elif choice == 3:
        print("Selected an Option to update an Student\'s data")
        getRollno = input("Enter the Roll no- ")
        getName = input("Enter the Name- ")
        getAdmno = input("Enter Admission Number- ")
        getCollege = input("Enter Collage Name- ")
        cursor = conn.execute("UPDATE STUDENT SET NAME='" + getName + "',ADMNO=" + getAdmno + ",COLLAGE='" + getCollege + "' WHERE ROLLNO=" + getRollno)
        conn.commit()
        print("Record Updated successfully")
        cursor = conn.execute("SELECT * FROM STUDENT WHERE ROLLNO=" + getRollno)
        for i in cursor:
            print("id-", i[0])
            print("Name-", i[1])
            print("Roll Numbers-", i[2])
            print("Admission Number-", i[3])
            print("College-", i[4])
            print("------------------------------------------------------")

    elif choice == 4:
        print("Selected an Option to delete an Student\'s data")
        getRollno = input("Enter the Roll no- ")
        cursor = conn.execute("DELETE FROM STUDENT WHERE ROLLNO=" + getRollno)
        conn.commit()
        print("Record deleted successfully")
        cursor = conn.execute("SELECT * FROM STUDENT")
        for i in cursor:
            print("id-", i[0])
            print("Name-", i[1])
            print("Roll Numbers-", i[2])
            print("Admission Number-", i[3])
            print("College-", i[4])
            print("------------------------------------------------------")
    elif choice == 5:
        break
    else:
        print("Invalid choice try again!!")

