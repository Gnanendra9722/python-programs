a1=input("enter str1:")
b1=input("enter str2:")
a=list(a1)
b=list(b1)
mark=0
if len(a)!=len(b):
    mark=1
else:
    n=len(a)
    for i in range(0,n-1+1):
        for j in range(0,n-2+1):
            if a[j]>a[j+1]:
                c=a[j]
                a[j]=a[j+1]
                a[j+1]=c
    for i in range(0,n-1+1):
        for j in range(0,n-2+1):
            if b[j]>b[j+1]:
                c=b[j]
                b[j]=b[j+1]
                b[j+1]=c

for i in range(0,n-1+1):
    if a[i]!=b[i]:
        mark=1
    else:
        mark=0
if mark==0:
    print('Anagram')
else:
    print("Not Anagram")




# def bubble_sort(s):
#     s = list(s)
#     n = len(s)
#     for i in range(n):
#         for j in range(n - 1):
#             if s[j] > s[j + 1]:
#                 c = s[j]
#                 s[j] = s[j + 1]
#                 s[j + 1] = c
#     return s

# a1 = input("enter str1: ")
# b1 = input("enter str2: ")

# a = bubble_sort(a1)
# b = bubble_sort(b1)

# mark = 0
# if len(a) != len(b):
#     mark = 1
# else:
#     for i in range(len(a)):
#         if a[i] != b[i]:
#             mark = 1
#             break
# if mark == 0:
#     print("Anagram")
# else:
#     print("Not Anagram")
