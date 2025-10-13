n=int(input("enter size of list:"))
list=[int(input("enter elem:")) for i in range(n)]
# for i in range(0,n-1+1):
#     x=int(input("enter x:"))
#     list.append(x)
print(list)
num=int(input("enter num to find:"))
c=0
for i in list:
    if i==num:
        c+=1
print(c)

