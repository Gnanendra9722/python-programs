n=int(input("enter number:"))
rev=0
while n!=0:
    r=n%10    #destruction
    n=n//10   #destruction

    rev=rev*10  #construction
    rev=rev+r   #construction

    print(r,rev) #optional for reference only  

print(rev)
