import threading

t = threading.currentThread().getName()
print(t)

#Changing the Name of the Thread

threading.currentThread().name = "New_Name_For_Thread"

print(threading.currentThread().getName())
