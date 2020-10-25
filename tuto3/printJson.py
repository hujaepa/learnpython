import json

jsonData = '{"name" : "huzai","age" : 29, "DOB" : "03/09/1991"}'

#use json.loads method#

myDict=json.loads(jsonData)#convert json to dictionary

for i in myDict:
	print(myDict[i])

