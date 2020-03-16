import threading
from threading import Thread


def odd_function():
    for x in range(20):
        if x%2 is not 0:
            print(x)

    print(threading.currentThread().getName())

def even_function():
    for x in range(20):
        if x%2 is 0:
            print(x)
    print(threading.currentThread().getName())

t1 = Thread(target=even_function)
t2 = Thread(target=odd_function)

t1.start()
t2.start()
