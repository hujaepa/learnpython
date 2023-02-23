myBio = {'name':'huzai','age':32,'hobby':'playing games'}

for key,value in myBio.items():
    print(key+":"+str(value))

myBio['name']='john'
print("----------")
for key,value in myBio.items():
    print(key+":"+str(value))