import time

@profile
def heavy_work():
    print('Do something')
    print('Do something')
    print('Do something')
    for _ in range(100_000):
        do_stuff()
    print('Do something')
    print('Do something')
    print('Do something')
def do_stuff():
    return 1 + 2

start_time = time.time()
heavy_work()
end_time = time.time()

print(end_time-start_time)