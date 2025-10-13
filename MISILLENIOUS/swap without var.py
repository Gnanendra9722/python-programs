a=int(input("a:"))
b=int(input("b:"))
def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    print("a:",a,"b:",b)
swap(a,b)


x=int(input("x:"))                       
y=int(input("y:"))
def swap(x,y):
    x=x*y
    y=x//y
    x=x//y
    print("x:",x,"y:",y)
swap(x,y)