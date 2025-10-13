class brain:
    def __init__(self):
        self.status="active"
    def getbrain(self):
        print(f"brain is {self.status}")
class car:
    def __init__(self,name):
        self.cname=name
    def getcar(self):
        print("person has car")
class person:
    def __init__(self,name):
        self.pname=name
        self.c=""
        self.b=brain()
    def hascar(self,p):
        self.c=p
p1=person("gnanee")
c1=car("bmw")
p1.hascar(c1)
print(p1.c.cname)
p1.c.getcar()
print(p1.b.status)
p1.b.getbrain()
del p1
print(c1.cname)
print(p1.o.status)

    