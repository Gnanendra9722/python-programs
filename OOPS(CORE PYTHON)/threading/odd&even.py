import time
from threading import Thread
done=False
class task1(Thread):
    def run(self):
        global done
        for i in range(100):
            if i%2==0:
                print(i)
                time.sleep(.5)
        done=True
class task2(Thread):
    def run(self):
        global done 
        while  not done:
            pass
        for i in range(100):
            if i%2!=0:
                print(i)
                time.sleep(.5)
t1=task1()
t2=task2()
t1.start()
t2.start()


