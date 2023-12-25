"""
Threads challenges are
    Synchronization threads
    Troubleshooting
    GIL

Synchronization threads
    Race conditions(a value might be modified by other process)
    Deadlocks(to solve issue of race conditions)
    Starvation(cannot acquire resources due to other threads)
    Livelocks(Crash or very slow performance, more threads acquire more locks on the resource)

Troubleshooting
    Reproducing
    Debugging
    Finding the root cause of the issues

GIL
    Only one thread is running
    The sleep() function releases the GIL
    Most impact on CPU - intensive tasks
"""

import threading
from time import sleep

def process_order(order_id):
    print(f"process starts with process_id: {order_id}")
    for _ in range(300_000_000):
        pass
    print(f"process ends with process_id: {order_id}")

thread1 = threading.Thread(target=process_order, args=(10,))
thread2 = threading.Thread(target=process_order, args=(20,))

thread1.start()
#thread2.start()
