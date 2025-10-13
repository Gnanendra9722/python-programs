n=int(input("enter size ofa:"))
a=[int(input("enter value:")) for i in range(n)]
n=int(input("enter size of b:"))
b=[int(input("enetr value:")) for i in range(n)]
print(a)
print(b)
res=[]
for i in b:
    if i not in a:
        res.append(i)
print(res)