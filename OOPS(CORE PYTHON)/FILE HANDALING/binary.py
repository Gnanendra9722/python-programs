ptr=open("E:\python\OOPS(CORE PYTHON)\FILE HANDALING\car.jpg",'rb')
data=ptr.read(3000)   #here it'll read only 3000 bytes to the newcar.jpg
print(data)
ptr.close()


#here we don't want to a previosly created newcar.jp it'll automatically created


ptr1=open("newcar.jpg","wb")
ptr1.write(data)   #imgae is copied to newcar.jpg
ptr1.close()

