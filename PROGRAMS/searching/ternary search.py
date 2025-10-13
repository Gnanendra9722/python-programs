#in ternary we calculate 2 mid values because of which array/list divided into 3 parts.
n=int(input("enter the size of list"))
list=[int(input("enter elem:")) for i in range(n)]
x=int(input("enter x to find:"))
i=0
j=n-1
mark=0
while i<=j:
    mid1=i+(j-i)//3
    mid2=j-(j-i)//3
    if x==list[mid1] or x==list[mid2]:
        print(f'{x} found at {mid1} index')
        mark=1
        break
    elif x<list[mid1]:
        j=mid1-1
    elif x>list[mid1] and x<list[mid2]:
        i=mid1+1
        j=mid2-1
    else:
        i=mid2+1
if mark==1:
    print("found")
else:
    print("not found")
    