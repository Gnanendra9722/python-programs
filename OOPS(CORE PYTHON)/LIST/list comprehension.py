l=[1,2,3,4,5]
l1=[i for i in l if i%2==0]
print(l1)


l2=[]
for i in l:
    if i%2==0:
        l2.append(i)

print(l2)