"""
Threads
    Seperate execution flows
    Part of a process
    Concurrency
    Improve Performance
    Lightweight
    Shared memory
    High potential for bugs
    GIL(Global Interpreter Lock) Constraint

Processes
    Heavyweight
    Separate memory
    Low potential for bugs
    No GIL constraint

"""

import threading
from time import sleep

def process_order(order_id):
    print(f"process starts with process_id: {order_id}")
    sleep(1)
    print(f"process ends with process_id: {order_id}")

thread1 = threading.Thread(target=process_order(10))
thread2 = threading.Thread(target=process_order(20))

thread1.start()
thread2.start()