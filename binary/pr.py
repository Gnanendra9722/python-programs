n=int(input("enter num:"))
list=[20,55,66,89,97,91,20]
tem=n
pos=0
sum=0
while tem>0:
    r=tem%2
    print(r)
    if r==1:
        sum=sum+list[pos]
    tem//=2
    pos+=1
print(sum)