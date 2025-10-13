a=input("enter a string:")
b=list(a)
capital=0
small=0
digit=0
special=0
words=0
space=0
for i in b:
    if i>='A' and i<='Z':
        capital+=1
    elif i>='a' and i<='z':
        small+=1 
    elif i>='0' and i<='9':
        digit+=1
    elif i==" ":
        space+=1
    else:
        special+=1
words=space+1
print("capital:",capital)
print("small:",small)
print("special:",special)
print("space:",space)
print("words:",words)
print("digit:",digit)



# a=input("enter a string:")
# capital=0
# small=0
# digit=0
# special=0
# words=0
# space=0
# for i in a:
#     if i>='A' and i<='Z':
#         capital+=1
#     elif i>='a' and i<='z':
#         small+=1 
#     elif i>='0' and i<='9':
#         digit+=1
#     elif i==" ":
#         space+=1
#     else:
#         special+=1
# words=space+1
# print("capital:",capital)
# print("small:",small)
# print("special:",special)
# print("space:",space)
# print("words:",words)
# print("digit:",digit)