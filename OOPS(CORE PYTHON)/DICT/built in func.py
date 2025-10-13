emp={"name":"gnanee","age":22,"exp":1}
print(emp)
emp["exp"]=2
print(emp)
print(emp["name"])


for i in emp:  #keys
    print(i)
for i in emp:  #values
    print(emp[i])



for i in emp.keys():
    print(i)

for i in emp.values():
    print(i)

for i in emp.items():
    print(i)