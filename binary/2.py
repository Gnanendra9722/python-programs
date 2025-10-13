l1=[5,2,1]
l2=[2,6,7]
l3=l1+l2
print(l3)
n=len(l3)
for i in range (n):
    for j in range(0,n-i-1):
        if l3[j]>l3[j+1]:
            l3[j],l3[j+1]=l3[j+1],l3[j]
print("sorted list:",l3)
if n%2==1:
    middle=l3[n//2]
else:
    middle=(l3[(n//2)-1]+l3[n//2])/2
print(middle)


