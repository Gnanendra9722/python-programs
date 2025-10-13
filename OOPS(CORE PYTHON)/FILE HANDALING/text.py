#  Write a program to take name as input from user and write it to a file named Write.txt
# name = input('enter a name : ')
# ptr = open('Write.txt','w')
# ptr.write(name)
# ptr.close()



#  Write a program to read the name from Write.txt and print it on the output screen.
# ptr1 = open('Write.txt','r')
# res = ptr1.read()
# print(res)
# ptr1.close()

#appending data to a file
# statement = input('enter a statement : ')
# ptr = open('Write.txt',"a")
# ptr.write(statement)
# ptr.close()

# Read types
# ptr = open('Write.txt','r')
# res = ptr.readlines()
# print(res)
# ptr.close()

# with open('Write.txt','r') as ptr:
#     res = ptr.read()
#     print(res)

# new_line = input('enter : ')
# with open('Write.txt','a') as ptr:
#     ptr.write(new_line)



# tell() and seek()

with open('Write.txt','r') as ptr:
    pos = ptr.tell()
    print(pos)
    res = ptr.read(5)
    print(res)
    pos1 = ptr.seek(6)
    print(pos1)
    pos2 = ptr.tell()
    print(pos2)
    print(ptr.read(6))