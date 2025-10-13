a=input("enter str:")
n=len(a)-1
s=0
while n>=0:
    if a[n]==" ":
        s+=1
    if s==2:
        break
    n-=1
n=n+1
while a[n]!=" ":
    print(a[n],end="")
    n+=1 
# while (n<=len(a)-1 and a[n]!=" "):
#     print(a[n],end="")
#     n+=1
# for i in range(n,len(a)-1):
#         print(a[i],end="")
#         if a[i]==" ":
#              break


