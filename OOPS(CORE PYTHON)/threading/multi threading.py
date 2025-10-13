import time
from threading import Thread
class task1(Thread):
    def run(self):
        l=['hi','bye','see you']
        for i in l:
            print(i)
            time.sleep(3)
class task2(Thread):
    def run(self):
        for i in range(10):
            print(i)
            time.sleep(2)
class task3(Thread):
    def run(self):
        a=10
        b=20
        print(a+b)
t1=task1()
t2=task2()
t3=task3()
t1.start()
t2.start()
t3.start()