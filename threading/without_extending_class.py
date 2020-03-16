import threading

from threading import Thread
class mythread:
    def even_numbers(self):
        for x in range(20):
            if x%2 is 0:
                print(x)



obj = mythread()
t = Thread(target=obj.even_numbers,name="even_thread")
t.start()
