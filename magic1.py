class ope:
    def __init__(self):
        self.l1=[]

    def accept(self):
        n=int(input("enter the Number of Elements for n:"))
        for i in range(0,n):
            e=int(input("Enter element: "))
            self.l1.append(e)
        print("list : ",self.l1)

    def __add__(self,other):
        newlist=[]
        for i in range(0,len(self.l1)):
            newlist.append(self.l1[i]+other.l1[i])
        print("After Addition : ",newlist)

    def __sub__(self,other):
        newlist=[]
        for i in range(0,len(self.l1)):
            newlist.append(self.l1[i]-other.l1[i])
        print("After Subtraction: ",newlist)
    
    def __mul__(self,other):
        newlist=[]
        for i in range(0,len(self.l1)):
            newlist.append(self.l1[i]*other.l1[i])
        print("After Multipication: ",newlist)

    def __floordiv__(self,other):
        newlist=[]
        for i in range(0,len(self.l1)):
            newlist.append(self.l1[i]//other.l1[i])
        print("After Floor Division: ",newlist)
    
