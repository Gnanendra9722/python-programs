class radio:
    def turnon(self,x):
        if x==1:
            print("radio is on")
        else:
            print("radio is off")
class car:
    def __init__(self,max,min):
        self.cmax=max
        self.cmin=min
        self.r=radio()
c1=car(30,140)
print(c1.cmax)
print(c1.cmin)
c1.r.turnon(1)
c1.r.turnon(0)