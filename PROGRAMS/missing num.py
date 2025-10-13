# list=[]
# n=int(input("enter size of list:"))
# for i in range(0,n-1):
#     x=int(input("enter x:"))
#     list.append(x)
# print(list)
# sum=0
# for i in list:
#     sum+=i
# miss=(n*(n+1))//2-sum
# print(miss)

# list=[]
# n=int(input("enter size of list:"))
# for i in range(0,n-1):
#     x=int(input("enter x:"))
#     list.append(x)
# print(list)
# sum1=1
# for i in list:
#     sum1*=i
# print(sum1)
# list2=[]
# n1=int(input("enter size of list:"))
# for i in range(0,n1-1+1):
#     x=int(input("enter x:"))
#     list2.append(x)
# print(list2)
# sum2=1
# for i in list2:
#     sum2*=i
# print(sum2)

# print(f"{sum2//sum1} is missing number")

list=[]
n=int(input("enter size of list:"))
for i in range(0,n-1):
    x=int(input("enter x:"))
    list.append(x)
print(list)
sum1=0
for i in list:
    sum1+=i
print(sum1)
list2=[]
n1=int(input("enter size of list:"))
for i in range(0,n1-1+1):
    x=int(input("enter x:"))
    list2.append(x)
print(list2)
sum2=0
for i in list2:
    sum2+=i
print(sum2)

print(f"{sum2-sum1} is missing number")



