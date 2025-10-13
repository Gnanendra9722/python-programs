a=input("enter str:")
b=list(a)
n=len(a)
mark=0
i=0
j=n-1
while i<j:
    if b[i]!=b[j]:
        mark=1
    i+=1
    j-=1   
if mark==0:
    print("palindrom")
else:
    print("not palindrom")  


