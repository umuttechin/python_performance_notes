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