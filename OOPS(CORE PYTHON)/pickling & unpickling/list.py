import pickle
l=["gnanedra",2,["sai","basha"],"chinnu"]


p1=open("list.txt",'wb')
pickle.dump(l,p1)
p1.close()


p2=open("list.txt","rb")
res=pickle.load(p2)
p2.close()
print(res)