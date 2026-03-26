# import threading

# # print(threading.current_thread().ident)
# # print(threading.current_thread().ident)
# # print(threading.current_thread().is_alive())

# # import Thread from threading
# from threading import Thread, current_thread
# import time

# # define functions
# def display(n, msg):
#     # print("T1 Thread: ", current_thread())
#     for num in range(n):
#         time.sleep(1)
#         print(msg)

# def display2(n, msg):
#     # print("T2 Thread: ", current_thread())
#     for num in range(n):
#         time.sleep(1)
#         print(msg)
# # create threads
# thread1 = Thread(target=display, args=(5, 'Hello World'))
# # print(thread1.ident)
# thread2 = Thread(target=display2, kwargs={'n':5, 'msg':'Bye Bye...'})
# # print(thread2.ident)
# # start thread
# # thread1.start()
# # print(f"Thread-1 Name: {thread1.name}")
# # print(f"Thread-1 Status: {thread1.is_alive()}")
# # print(f"Thread-1 id: {thread1.ident}")
# # thread1.join()
# # thread2.start()


# def square(n):
#     return n*n


# def cube(n):
#     return n**n

# start_time = time.perf_counter()
# n = 3
# thread1 = Thread(target=square, args=(n, ))
# thread2 = Thread(target=cube, args=(n, ))
# thread1.start()
# thread2.start()
# time_taken = time.perf_counter() - start_time
# # print("Time Taken in multithreading: ", time_taken)

# start = time.perf_counter()
# d1 = square(n)
# d2 = cube(n)
# total = time.perf_counter() - start
# # print(f"Time taken in normal way: {total}")


# from time import sleep
# from threading import *

# myLock = Semaphore()

# def displayMsg(myLock, msg):
#     myLock.acquire()
#     for x in range(5):
#         print(msg)
#     sleep(2)
#     myLock.release()

# t1 = Thread(target=displayMsg, args=(myLock, "Hello World"))
# t2 = Thread(target=displayMsg, kwargs={'myLock': myLock, 'msg':"Hello Python"})
# t1.start()
# t2.start()

from time import sleep
import threading
from queue import Queue
my_q = Queue()
def readFile(my_q):
    with open("new.txt", "r") as f1:
        readLines = f1.readlines()
        count = 0
        for lineNos in range(0, len(readLines), 5):
            chunkSize = readLines[lineNos:lineNos+5]
            count = count+len(chunkSize)
            print(f"No of lines read {count}")
            my_q.put(chunkSize)
        my_q.put(None)
            
def writeFile(my_q):    
    with open("new1.txt", "w") as f2:
        while True:        
            readLine = my_q.get()
            if readLine is None:
                break            
            f2.writelines(readLine)

t1 = threading.Thread(target=readFile, args=(my_q,))
t2 = threading.Thread(target=writeFile, args=(my_q,))
t1.start()
t2.start()
