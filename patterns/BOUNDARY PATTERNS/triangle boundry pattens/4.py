# * * * * * 
#   *     * 
#     *   *
#       * *
#         *

n=5
for i in range(1,5+1,1):
    for j in range(1,5+1,1):
        if j==5 or i==1 or i==j:
            print("* ",end="")
        else:
            print("  ",end="")   
    print("") 