n=int(input("enter n:"))
o=n
rev=0
while n!=0:
    r=n%10
    n//=10
    rev=rev*10
    rev=rev+r
print(rev)
if rev==o:
    print("palindrome")
else:
    print("not palindrome")