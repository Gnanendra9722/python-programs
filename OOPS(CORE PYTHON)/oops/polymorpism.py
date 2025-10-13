class plane:
    def takeoff(self):
        print("plane is taking off")
    def fly(self):
        print("plane is flying")
class passanger(plane):
    def land(self):
        print("plane is landing")
class cargo(plane):
    def land(self):
        print("cargo is landing")
class fighter(plane):
    def land(self):
        print("plane is landing")
p1=passanger()
c1=cargo()
f1=fighter()
def allowplane(ref):
    ref.takeoff()
    ref.fly()
    ref.land()
allowplane(p1)
allowplane(c1)
allowplane(f1)
