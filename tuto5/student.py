class Person:
	def display(self,fname,lname):
		print("First Name : "+fname)
		print("Last Name : "+lname)

class Student(Person):
	def __init__(self,fname,lname):
		self.firstname=fname
		self.lastname=lname
		super().display(self.firstname,self.lastname)