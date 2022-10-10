n=int(input("Enter no.of employ:"))
l=[]
bonus=100
total=0
names=[]
for i in range(n):
    name=input("Enter employee name:")
    names.append(name)
    sal=int(input("Enter salary:"))
    l.append(sal)
    id=input("enter id:")
    exp=int(input("Enter experience:"))
    if exp<=2:
        print("No bonus")
        print("net salary",sal)
        print("HRA",sal*0.20)
        print("DA",sal*0.5)
        print("TA",sal*0.1)
    else:
        net_sal=sal+bonus
        print("Net salary of the employee is:",net_sal)
        print("HRA",sal*0.20)
        print("DA",sal*0.5)
        print("TA",sal*0.1)
print("name:salary")
for i in range(n):
    print(names[i],":",l[i])
l=sorted(l)
print("Highest salary:",l[-1])
print("Lowest salary:",l[0])
for i in range(n):
    total=total+l[i]
avg=total/n
print("Average salary is",avg)
      