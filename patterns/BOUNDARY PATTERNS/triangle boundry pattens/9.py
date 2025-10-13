# *  *  *  *  *  *  *  *  *  *  *  
# *  *           *           *  *  
# *     *        *        *     *
# *        *     *     *        *
# *           *  *  *           *
# *  *  *  *  *  *  *  *  *  *  *
# *           *  *  *           *
# *        *     *     *        *
# *     *        *        *     *
# *  *           *           *  *
# *  *  *  *  *  *  *  *  *  *  *

n=11
for i in range(1,11+1,1):
    for j in range(1,11+1,1):
        if i==1 or i==11 or j==1 or j==11 or i==6 or j==6 or i==j or i+j==n+1 :
            print("* ",end=" ")
        else:
            print("   ",end="")
    print("")