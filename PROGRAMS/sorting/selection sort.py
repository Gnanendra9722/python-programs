n=int(input("enter size of list:"))
list=[int(input("enter elem:")) for i in range(n)]
print(list)
for i in range(0,n-2+1):
    for j in range(i+1,n-1+1):
        if list[i]>list[j]:
            c=list[i]
            list[i]=list[j]
            list[j]=c
print(list)