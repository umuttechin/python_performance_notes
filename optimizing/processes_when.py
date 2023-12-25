"""
Multiprocessing
    More processes
    Can use more CPU cores
    CPU - intensive tasks
    More isolated

Threading/Asyncio
    One or more threads in a process
    Can use only one CPU core
    I/O - intensive task
    Less isolated

Use Cases
    Data pipeline
    Producer - consumer applications
    Parallelizable workloads

Implementing Multiprocess Applications
    Use logging and monitoring
    Terminate cleanly
    Access to shared resources
    Limit the number of processes(50 processes on 4 CPU cores)

"""

from multiprocessing import Process

def clean_order_process(order_id):
    for _ in range(500_000_000):
        pass
    print(f"finished process {order_id}.")


if __name__ == '__main__':
    p1 = Process(target=clean_order_process, args=(10,))
    p2 = Process(target=clean_order_process, args=(20,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
