a=input("enter str:")
b=list(a)
n=len(a)
for i in range(0,n-1+1):
    for j in range(0,n-2+1):
        if b[j]>b[j+1]:
            c=b[j]
            b[j]=b[j+1]
            b[j+1]=c
a=""
for i in b:
    a=a+i
print(a)

# a = input("enter str: ")
# n = len(a)

# # convert string to mutable form by using slicing
# for i in range(n):
#     for j in range(n - 1):
#         if a[j] > a[j + 1]:
#             # swap characters using slicing
#             a = a[:j] + a[j+1] + a[j] + a[j+2:]
#             print(a)

# print(a)
