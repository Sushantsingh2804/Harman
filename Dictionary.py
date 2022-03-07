Count = int(input("Enter the number of books: "))
Books_list = []
Books_dic = {}
for i in range(0, Count):
    Books_dic = {
        "Name": input("Enter the name of book "+str(i+1)+": "),
        "Publisher": input("Enter the Publisher of book "+str(i+1)+": "),
        "Year of publication": input("Enter the year of Publication of book "+str(i+1)+": ")
    }
    Books_list.append(Books_dic)
print(Books_list)

for Book in Books_list:
    print("Details of book ", Books_list.index(Book)+1)
    for x, y in Book.items():
        print(x, ": ", y)
