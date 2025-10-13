n=int(input("enter a number:"))
c=0
for i in range(1,n+1):
    if n%i == 0:
        c+=1
        print(f"{c}:{i}",end=" ")
print("")
print("count is :",c)
