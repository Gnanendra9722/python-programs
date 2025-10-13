a=set()
for i in range(5):
    data=int(input("enyer a value:"))
    a.add(data)
print(a)

a.update([6,7])
print(a)

a.discard(7)
print(a)


