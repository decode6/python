class Employee:
    apply_raise=1.5
    def __init__(self,first,last,empid,pay):
        self.first=input("Enter the First name")
        self.last=input("Enter the Last name")
        self.empid=input("Enter the Emp ID")
        self.pay=int(input("Enter the Salary"))

    def display(self):
        print("first name:", self.first)
        print("last name:", self.last)
        print("empid=",self.empid)
        print("pay=", self.pay)

    def pay_raise(self):
        self.pay=int(self.pay)*self.apply_raise

class Developer(Employee):
    apply_raise=2.5
    def pay_raise(self):
        self.pay=int(self.pay)*self.apply_raise

class Manager(Employee):
    apply_raise=3.5
    def pay_raise(self):
        self.pay=int(self.pay)*self.apply_raise

e1=Employee("sachin", "bgd"," mca", "20")
e2=Manager("Akash","DL", "mca1", "22")
e1.pay_raise()
e2.pay_raise()
e1.display()
e2.display()


