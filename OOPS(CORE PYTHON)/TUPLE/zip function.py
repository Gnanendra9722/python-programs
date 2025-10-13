x=["virat","msd","gayle","rohit"]
y=[18,7,333,45]
z=["ind","ind","wi","ind"]
a=["rcb","csk","punj","mi"]

c=[(x[0],y[0],z[0],a[0]),(x[1],y[1],z[1],a[1]),(x[2],y[2],z[2],a[2]),(x[3],y[3],z[3],a[3])]
print(c)

l=list(zip(x,y,z,a))
print(l)



x=["virat","msd","gayle","rohit"]
y=[18,7,333,45]
z=["ind","ind"]
a=["rcb","csk"]
l=list(zip(x,y,z,a))
print(l)




from itertools import zip_longest
x=["virat","msd","gayle","rohit"]
y=[18,7,333,45]
z=["ind","ind"]
a=["rcb","csk"]


l=list(zip_longest(x,y,z,a))
print(l)



from itertools import zip_longest
x=["virat","msd","gayle","rohit"]
y=[18,7,333,45]
z=["ind","ind"]
a=["rcb","csk"]
l=list(zip_longest(x,y,z,a,fillvalue="#"))
print(l)