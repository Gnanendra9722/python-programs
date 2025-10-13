# a=int(input("enter a:"))
# b=int(input("enter b:"))
# hcf=0
# for i in range (1,a+1):
#     if a%i==0 and b%i==0: 
#         hcf=i
# print("hcf =",hcf)
# lcm=((a*b))//hcf

# print("lcm =",lcm)


# for lcm
a=int(input("enter a:"))
b=int(input("enter b:"))
greater=a if a>b else b
while True:
    if greater%a==0 and greater%b==0:
        lcm=greater
        break
    greater+=1
print(lcm)


