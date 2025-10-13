list=[]
n=int(input("enter size of list:"))
for i in range(0,n-1+1):
    x=int(input("enter x:"))
    list.append(x)
print(list)
i=0
j=n-1
while i<j:
    c=list[i]
    list[i]=list[j]
    list[j]=c
    i+=1
    j-=1
print(list)
        