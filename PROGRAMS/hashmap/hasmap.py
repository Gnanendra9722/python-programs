pos=[0 for i in range(10)]
nec=[0 for i in range(10)]
print(pos)
print(nec)
n=int(input("enter n:"))
for i in range(0,n-1+1):
    x=int(input("enter x:"))
    if x>=0:
        pos[x]+=1
    else:
        x=x*-1
        nec[x]+=1

print(pos)
print(nec)