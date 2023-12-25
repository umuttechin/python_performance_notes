import threading
def clean_order_thread(order_id):
    for _ in range(500_000_000):
        pass
    print(f"finished thread {order_id}.")




if __name__ == '__main__':
    p1 = threading.Thread(target=clean_order_thread, args=(10,))
    p2 = threading.Thread(target=clean_order_thread, args=(20,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()