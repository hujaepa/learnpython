import random
def genTempPassword(name):
    tempPassword = name.upper().replace(" ","")+str(random.randint(1,5))
    return tempPassword

def genEmail(name):
    splitName = name.split(' ',1) #will split the name when encounter the first space
    email = splitName[0].lower()+"@apu.edu.my"
    return email
