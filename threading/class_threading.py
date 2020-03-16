import threading
from threading import Thread

class myThread(Thread):
    def run(self):
        for i in range(0,5):
            for j in range(0,i+1):
                print("x ",end=" ")
            print("\n")

obj = myThread()
obj.start()
