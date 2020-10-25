bio = [{
	"name" : "huzai",
	"age" : 29,
	"DOB" : "03/09/1991"
},
{
	"name" : "mrhu",
	"age" :21,
	"DOB" : "03/09/2000"
}]

for i in range(0,len(bio)):
	print("Name : "+bio[i]["name"])
	print("Age : "+str(bio[i]["age"]))
	print("DOB : "+bio[i]["DOB"])
	print("=============")