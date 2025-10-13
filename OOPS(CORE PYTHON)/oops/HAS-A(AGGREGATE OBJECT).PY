class charger:
    def __init__(self,name):
        self.cname=name
    def getcharger(self):
        print("mobile is charging")
class mobile:
    def __init__(self,name):
        self.mname=name
        self.c=""
    def hasmobile(self,p):
        self.c=p
m1=mobile("iphone")
c1=charger("type c")
m1.hasmobile(c1)
print(m1.c.cname)
m1.c.getcharger()
del m1
print(c1.cname)#here we can access charger without main obj(mobile) 


