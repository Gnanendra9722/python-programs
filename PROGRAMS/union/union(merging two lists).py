n=int(input("enter size ofa:"))
a=[int(input("enter value:")) for i in range(n)]

n=int(input("enter size of b:"))
b=[int(input("enetr value:")) for i in range(n)]
union=[]
for i in a:
    union.append(i)
for i in b:
    if i not in union:
        union.append(i)
print("a=",a)
print("b=",b)
print("union=",union)