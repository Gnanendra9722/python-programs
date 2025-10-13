a=input("enter str1:")
b=input('enter str2:')
c=''
index=int(input("index:"))
for i in range(0,index-1+1):
    c=c+a[i]
c=c+b
for i in range(index,len(a)-1+1):
    c=c+a[i]
print(c)
