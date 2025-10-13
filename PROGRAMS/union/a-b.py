n=int(input("enter size ofa:"))
a=[int(input("enter value:")) for i in range(n)]
print(a)
n=int(input("enter size of b:"))
b=[int(input("enetr value:")) for i in range(n)]
print(b)
res=[]
for i in a:
    if i not in b:
        res.append(i)
print(res)