# n=int(input("enter n:"))
# o=n
# length=len(str(o))
# rev=0
# while n!=0:
#     r=n%10
#     n=n//10
#     rev=rev+r**length
# if rev==o:
#     print("amstrong")
# else:
#     print("not amstrong")

n=int(input("enter n:"))
save=n
len=0
while n!=0:
    n=n//10
    len=len+1
print(len)
n=save
arm=0
while n!=0:
    r=n%10
    n=n//10
    arm=arm+r**len
n=save
if arm==n:
    print("number is armstrong")
else:
    print("not a armstrong number")
    
# n=int(input("enter n:"))
# save=n
# len=0
# ams=0
# while n!=0:
#     r=n%10
#     n//=10
#     len+=1
# print(len)
# n=save
# while n!=0:
#     r=n%10
#     n=n//10
#     ams=ams+(r**len)
# print(ams)
# n=save
# if ams==n:
#     print("armstrong")
# else:
#     print("not armstrong")