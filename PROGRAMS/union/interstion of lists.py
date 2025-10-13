n=int(input("enter size ofa:"))
a=[int(input("enter value:")) for i in range(n)]

n=int(input("enter size of b:"))
b=[int(input("enetr value:")) for i in range(n)]
intersection=[]
for i in a:
    if i in b:
        intersection.append(i)
print(intersection)