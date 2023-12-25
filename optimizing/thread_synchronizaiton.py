"""
How to Synchronization threads
    Locks
    Semaphores(for example; limit hte number of connections to a database)
    Condition variables(for example; condition variable notify any waiting threads the resource has just been updated)

Use Threads
    Tasks that wait for external events
    Blocking I/O
    Simple logic

Do Not Use Threads
    No waiting for external events
    CPU - extensive tasks
    Complex logic

--------------------------------

kernprof -lv thread_synchronizaiton.py
Wrote profile results to thread_synchronizaiton.py.lprof
Timer unit: 1e-06 s

Total time: 2.37569 s
File: thread_synchronizaiton.py
Function: main at line 39

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    39                                           @profile
    40                                           def main():
    41         1    1905788.0    2e+06     80.2      single_thread()
    42         1     469903.0 469903.0     19.8      multithread()

"""

import threading
from time import sleep
from urllib import request

def download():
    return request.urlopen("https://google.com").read()

def single_thread():
    for _ in range(5):
        download()

def multithread():
    threads = []
    for _ in range(5):
        threads.append(threading.Thread(target=download))
    for t in threads:
        t.start()
    for t in threads:
        t.join()

@profile
def main():
    single_thread()
    multithread()

main()
