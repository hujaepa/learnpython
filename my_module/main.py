from helper import genTempPassword as tempPassword
from helper import genEmail as email

name = "James Willems"
print(name)
print(f"{tempPassword(name)}")
print(f"{email(name)}")