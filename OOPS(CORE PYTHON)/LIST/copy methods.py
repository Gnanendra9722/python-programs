l=[10,20,30,40,50]
l1=l
print(l)
print(l1)
l[2]=30.5
print(l)
print(l1)

print("=======================================================================================")

l=['divya','gonu',[10,20,30,40,50],'fonu']
l1=l.copy()   #deep copy
print(l)
print(l1)
l[2][1]=30.5
print(l)
print(l1)
l[1]="bindu"
print(l)
print(l1)

print("===================================================================================================")
import copy
l=['divya','gonu',[10,20,30,40,50],'fonu']
l1=copy.deepcopy(l)   #deep copy
print(l)
print(l1)
l[1]=30.5
print(l)
print(l1)