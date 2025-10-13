n=int(input("size of list:"))
a=[int(input("a:")) for i in range(n)]
x=int(input("enter x:"))#80
i=0
j=n-1
mark=0
while i<=j:
    mid=(i+j)//2
    if x==a[mid]:
        print(f"{x} found at {mid} index")
        mark=1
        break
    elif x>a[mid]:
        i=mid+1
    else:
        j=mid-1
if mark==0:
    print("not found")










