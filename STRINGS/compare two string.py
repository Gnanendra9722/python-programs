a=input("enter st1:")
b=input("enter str2:")
mark=0
if len(a)!=len(b):
    mark=1
else:
    n=len(a)
    for i in range(0,n-1+1):
        if a[i]!=b[i]:
            mark=1
            break #not reqired but reduce time of complexcity
if mark==0:
    print("equal")
else:
    print('different')
