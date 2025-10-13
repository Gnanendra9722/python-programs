# private
# class book:
#     def __init__(self,page):
#         self.__pages=page #use 2 undescore private
# c1=book(100)
# print(c1.__pages)  #error





# To access and modify private variable
class book:
    def __init__(self,page):
        self.__pages=page #use 2 undescore private
    def setter(self,val):
        if val>0:
            self.__pages=val
    def getter(self):
        return self.__pages
c1=book(100)
res1=c1.getter()
print(res1)
c1.setter(200)
res2=c1.getter()
print(res2)
c1.setter(-199)
res3=c1.getter()
print(res3)