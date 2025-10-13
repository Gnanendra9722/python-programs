#         * 
#       * * 
#     *   *
#   *     *
# * * * * *

n=5
for i in range (1,5+1,1):
    for j in range(1,5+1,1):
        if j==5 or i==5 or i+j==n+1:
            print("* ",end="")
        else:
            print("  ",end="")
    print("")