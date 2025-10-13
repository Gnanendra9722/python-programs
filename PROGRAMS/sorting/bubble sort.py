# list=[10,6,17,2,3,1]
# for i in range(len(list)):
#     for j in range(0,len(list)-1):
#         if list[j]>list[j+1]:
#             list[j],list[j+1]=list[j+1],list[j]
#         print(list)


n=int(input("enter size of list:"))
list=[int(input("enter elem:")) for i in range(n)]
# for i in range(0,n-1+1):
#     x=int(input("enter x:"))
#     list.append(x)
print(list)
for i in range(0,len(list)-1+1):
    for j in range(0,len(list)-2+1):
        if list[j]>list[j+1]:
            c=list[j]
            list[j]=list[j+1]
            list[j+1]=c
print(list)