'''
MULTITHREADING:
Execute parallelly.
'''


import threading
import time

def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

# normal code
# func(5)
# func(4)
# func(3)
# func(2)
# func(1)

# code using threads
time1= time.perf_counter()
t1 = threading.Thread(target=func, args=[5])
t2 = threading.Thread(target=func, args=[4])
t3 = threading.Thread(target=func, args=[3])
t4 = threading.Thread(target=func, args=[2])
t5 = threading.Thread(target=func, args=[1])

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
time2= time.perf_counter()
print(time2-time1) 