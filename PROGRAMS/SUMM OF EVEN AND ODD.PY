list=[]
n=int(input("enter size of list:"))
for i in range(0,n-1+1):
    x=int(input("enter x:"))
    list.append(x)
print(list)
evensum=0
oddsum=0
for i in list:
    if i%2==0:
        evensum+=i
    else:
        oddsum+=i
# for i in range(0,n-1+1):
#     if list[i]%2==0:
#         evensum+=list[i]
#     else:
#         oddsum+=list[i]
print(f"{evensum} is even sum")
print(f"{oddsum} is odd sum")