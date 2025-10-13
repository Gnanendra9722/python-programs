id=[101,102,103,104]
name=['aagu','badhri','krishna','rukhmini']

res1=dict(zip(id,name))
print(res1)

mob=[95,89,34,98]
add=['russia','nigeria','thailand','india']
# res2=dict(zip(id,name,mob,add))    #ERROR ,(we want to pass only two list)
# print(res2)


data=list(zip(name,mob,add))
res3=dict(zip(id,data))
print(res3)