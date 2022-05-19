d={}
class student:
	def __init__(self):
		self.usn=input("Enter usn")
		self.name=str(input("Enter name"))
		self.age=int(input("Enter age"))
	def display(self):
		print("name :",self.name)
		print("usn :",self.usn)
		print("age :",self.age)
class deriv1(student):
	def __init__(self):
		student.__init__(self)
		self.sem=input("Enter sem")
		self.sub=[]
		self.total=0
		for i in range(1,6):
			m=int(input("enter marks in sub "))
			self.sub.append(m)
			self.total+=m
		self.per=(self.total/250)*100
		deriv1.display(self)
	def display(self):
		student.display(self)
		print("SEMESTER :",self.sem)
		for i in range(5):
			print("marks in sub are ",self.sub[i])
		print("percent =",self.per)
class deriv2(deriv1):
	def __init__(self):
		deriv1.__init__(self)
		d.update({self.name:{
		"name":self.name,
		"usn":self.usn,
		"age":self.age,
		"semester":self.sem,
		"sub":self.sub,
		"total":self.total,
		"percent":self.per
		}})
def printtemp():
	for key in d:
		print(key,d[key])
while True:
	print("1.add 2.display 3.exit")
	ch=int(input("enter the choice"))
	if ch==1:
		d2=deriv2()
	elif ch==2:
		printtemp()
	elif ch==3:
		break
