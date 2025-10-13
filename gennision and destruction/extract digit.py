n=int(input("enter a number"))
print(n)
while n!=0:
    r=n%10
    n=n//10
    print(r," ",n)