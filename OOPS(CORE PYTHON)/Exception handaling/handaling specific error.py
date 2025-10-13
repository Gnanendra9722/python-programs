try:
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    res=a/b
    print(res)
except ValueError as e:     #if b or a given as five like that insted of 5
    print("error is value error")
except ZeroDivisionError as e:
    print("error is zerodivisionerror")
except Exception as e:   #let int remove for b but given as 5 then this block excetute
    print("error occured")
    print(e)



try:
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    res=a/b
    print(res)
except (ValueError,ZeroDivisionError) as e:     #if b or a given as five like that insted of 5
    print("error is value error or zero division error")
except Exception as e:   #let int remove for b but given as 5 then this block excetute
    print("error occured")
    print(e)



try:
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    res=a/b
    print(res)
except Exception as e:     #if b or a given as five like that insted of 5
    print("error is value error or zero division error")
    print(e.__str__())
