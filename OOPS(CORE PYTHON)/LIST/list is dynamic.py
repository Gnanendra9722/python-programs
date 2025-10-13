l=[]
i=0
while True:
    n=int(input("enter  a number:"))
    l.insert(i,n)
    i+=1
    print("do you want to continue")
    print("press 1 for yes 2 for no")
    cho=int(input())
    if cho==1:
        continue
    else:
        break
print(l)


l=["JAANU",30,[10.2,40.4,"LILLI",["FONU","KOLU"]],40,50]
print(l[2][3][1])