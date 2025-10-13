n=4
for i in range (1,4+1):
    for j in range (1,4+1):
        if i+j==n+1:
            print("*",end="")
        else:
            print(" ",end="")
    for j in range (1,4+1):
        if i==j+1:
            print("*",end="")
        else:
            print(" ",end="")
    print("")  

n=3
for i in range (1,3+1):
    for j in range (1,3+1):
        if i==j-1:
            print("*",end="")
        else:
            print(" ",end="")
    for j in range (1,3+1):
        if i+j==n+1:
            print("*",end="")
        else:
            print(" ",end="")
    print("")  

      