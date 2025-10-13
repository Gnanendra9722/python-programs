list=[]
n=int(input("enter size of list:"))
for i in range(0,n-1+1):
    x=int(input("enter x:"))
    list.append(x)
print(list)
sum=0
for i in list:
    sum+=i
print(sum)