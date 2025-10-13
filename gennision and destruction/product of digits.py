n=int(input("enter a number"))
p=1
while n!=0:
    r=n%10
    n=n//10
    p*=r
print(p)