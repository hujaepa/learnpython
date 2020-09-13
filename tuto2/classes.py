class Bio:
    def __init__(this,name,age,occupation):
        this.name=name
        this.age=age
        this.occupation=occupation

    def getName(this):
        print("Name : "+this.name)
    
    def getAge(this):
        print("Age : "+str(this.age))
    
    def getOccupation(this):
        print("Occupation : "+this.occupation)
    
bio = Bio("Huzai",29,"Programmer")
bio.getName()
bio.getAge()
bio.getOccupation()