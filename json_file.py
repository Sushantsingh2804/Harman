import json

data = {"name": "Sushant","Status": "Student"}
myJsonData = json.dumps(data)
myJsonfile=json.loads(myJsonData)
print(myJsonData, myJsonfile)

