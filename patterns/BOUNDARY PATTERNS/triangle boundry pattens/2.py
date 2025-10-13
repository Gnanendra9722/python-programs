# *
# * *       
# *   *
# *     *
# * * * * *

for i in range(1,5+1,1):
    for j in range(1,5+1,1):
        if j==1 or i==5 or i==j:
            print("* ",end="")
        else:
            print("  ",end="")
    print("")            