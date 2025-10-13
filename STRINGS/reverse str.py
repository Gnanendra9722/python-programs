a=input("enter str:")
b=list(a)
print(b)
n=len(a)
i=0
j=n-1
while i<j:
    c=b[i]
    b[i]=b[j]
    b[j]=c
    i+=1
    j-=1
print(b)
a=""
for i in b:
    a=a+i
print(a)