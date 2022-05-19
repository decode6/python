print("1.size of set")
print("2.length of set")
print("3.add of set")
print("4.intersection of set")
print("5.diffrence of set")
print("6.symmetric diffrence of set")
print("7.check for a element of set")
print("8.pop of set")
print("9.clearing of set")
print("10.deletion of set")
print("0.exit")
while True:
    ch=int(input("enter your choice"))
    if ch==1:
        set1=set(input("enter the set"))
        print(set1.__sizeof__())
    elif ch==2:
        set1=set(input("enter the set"))
        print(len(set1))
    elif ch==3:
        set1=set(input("enter the set"))
        set1.add(7)
        print(set1)
    elif ch==4:
        set1=set(input("enter the set1"))
        set3=map(int,set1)
        set2=(input("enter the set2"))
        set4=map(int,set2)
        print(set3.i)
    elif ch==5:
        set1=set(input("enter the set1"))
        set2=set(input("enter the set2"))
        print(set1-set2)
    elif ch==6:
        set1=set(input("enter the set1"))
        set2=set(input("enter the set2"))
        print(set1^set2)
    elif ch==7:
        set1=set(input("enter the set"))
        print(set1.__contains__(8))
    elif ch==8:
        set1=set(input("enter the set"))
        set1.pop()
    elif ch==9:
        set1=set(input("enter the set"))
        set1.clear()
    elif ch==10:
        set1=set(input("enter the set"))
        del(set1)
        print(set1)
    elif ch==0:
        exit()
    break
       
