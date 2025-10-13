import time
class demo:
    def printname(self):
        l=["hi",'bye',"see you"]
        for i in l:
            print(i)
            time.sleep(3)
    def printnumbers(self):
        for i in range(10):
            print(i)
            time.sleep(2)
    def add(self):
        a=10
        b=20
        print(a+b)
d=demo()
d.printname()
d.printnumbers()
d.add()