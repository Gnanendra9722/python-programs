# #construction
print("construction of num:")
b=0
for i in range(1,4+1):
        b*=10  #socket creation(units place)
        b+=i    #adding unit digit
        print(b)    # to print all steps [optional]
print(b)


# #destruction
print("destruction of num:")
b=1234
while b!=0:
    r=b%10  #extraction
    b=b//10  #disappear
    print(r," ",b)


#construction some other logic

# b=0
# while b!=1792:
#         b*=10  #socket creation(units place)
#         n=int(input("enter a number to add:"))
#         b+=n    #adding unit digit
#         print(b)    # to print all steps [optional]
# print(b)


