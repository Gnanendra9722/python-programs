import pickle
class employee:
    def __init__(self,name,age):
        self.ename=name
        self.eage=age
    def disp(self):
        print(self.ename)
        print(self.eage)
# e=employee("gnanendra",22)


a=open("text.txt",'rb')
c=pickle.load(a)
a.close
c.disp()