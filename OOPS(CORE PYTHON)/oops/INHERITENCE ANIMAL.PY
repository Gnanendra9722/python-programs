class animal:
    def eat (self):
        print("animal is eating")
    def sleep(self):
        print("animal is sleeping")
    def hunt(self):
        print("animal is hunting")
class tiger(animal):
    pass
class hyena(animal):
    pass
class monkey(animal):
    pass
t1=tiger()
h1=hyena()
m1=monkey()
h1.eat()
m1.eat()
t1.eat()

