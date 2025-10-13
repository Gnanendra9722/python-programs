import pickle
class employee:
    def __init__(self,name,age):
        self.ename=name
        self.eage=age
    def disp(self):
        print(self.ename)
        print(self.eage)
e=employee("gnanendra",22)


# This one is for pickling
f=open("text.txt",'wb')
pickle.dump(e,f)
f.close()


a=open("text.txt",'rb')
c=pickle.load(a)
a.close()
c.disp()