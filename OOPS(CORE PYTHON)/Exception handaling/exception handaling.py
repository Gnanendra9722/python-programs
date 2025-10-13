def fun():
    a=10
    b=0
    c=a/b
try:
    fun()
except Exception as e:
    print(e,"error is occur")


def fun1(a,b):
    try:
        res=a/b
    except Exception as a:
        print("ERROR")
        raise a
fun1(10,0)