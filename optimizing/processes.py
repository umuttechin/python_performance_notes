"""
Limitations of Multithreaded and Asynchronous Code
    Potential for bugs
    Learning curve
    CPU intensive tasks(due to they use only one CPU core)

More Processes
    Seperate memory space
    No GIL for processes
    Utilize all CPU cores
    Increased memory overhead
    Harder to share resources

-----------------------------------------

from multiprocessing import Process

def clean_order():
    for _ in range(500_000_000):
        pass
    print("finished.")

if __name__ == '__main__':
    p1 = Process(target=clean_order)
    #p2 = Process(target=clean_order)

    p1.start()
    #p2.start()
    p1.join()
    #p2.join()
    
-----------------------------------------

time python processes.py
finished.
python3 processes.py  4.93s user 0.02s system 99% cpu 4.974 total

from multiprocessing import Process

def clean_order():
    for _ in range(500_000_000):
        pass
    print("finished.")

if __name__ == '__main__':
    p1 = Process(target=clean_order)
    p2 = Process(target=clean_order)

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
-----------------------------------------

time python processes.py
finished.
python3 processes.py  4.93s user 0.02s system 99% cpu 4.974 total

"""
from multiprocessing import Process

def clean_order():
    for _ in range(500_000_000):
        pass
    print("finished.")

if __name__ == '__main__':
    p1 = Process(target=clean_order)
    p2 = Process(target=clean_order)

    p1.start()
    p2.start()
    p1.join()
    p2.join()
