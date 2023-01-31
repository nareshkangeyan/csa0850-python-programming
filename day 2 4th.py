a=[]
b=[]
n=int(input("enter number of elements in list1"))
m=int(input("enter number of elements in list2"))
for i in range (1,n+1,1):
    e=int(input("enter elements of list1"))
    a.append(e)
print("list1",a)
for j in range (1,n+1,1):
    f=int(input("enter elements of list2"))
    b.append(f)
print("list2",b)
c=a+b
c.sort()
print("sorted list",c)
if a==[] and b==[]:
    print("output []")
