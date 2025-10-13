# cric={'name':'dhoni',
#       'age':42
#       }

# print(cric)
# c1=cric
# c2=cric.copy()
# print(c1)
# print(cric)
# print(c2)
# cric['age']=43
# print(c1)
# print(cric)
# print(c2)



#acheive deep copy in nested dict
import copy
heroien={"name":"sam",
         'age':39,
         "bf":{'name1':"chai",
               'name2':'rak'}
               }
h1=heroien.copy()
h2=copy.deepcopy(heroien)
print(h1)
print(heroien)
print(h2)
heroien['bf']['name3']='sek'
print(h1)
print(heroien)
print(h2)
