from threading import Thread

def even_function():
    for x in range(20):
        if x%2 is 0:
            print(x)

t = Thread(target=even_function)
t.start()
