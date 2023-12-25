"""
pip install line_profiler

kernprof -lv profiler2.py 
Do something
Do something
Do something
Do something
Do something
Do something
0.06821489334106445
Wrote profile results to profiler2.py.lprof
Timer unit: 1e-06 s

Total time: 0.037437 s
File: profiler2.py
Function: heavy_work at line 3

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     3                                           @profile
     4                                           def heavy_work():
     5         1         95.0     95.0      0.3      print('Do something')
     6         1          5.0      5.0      0.0      print('Do something')
     7         1          5.0      5.0      0.0      print('Do something')
     8    100001      13621.0      0.1     36.4      for _ in range(100_000):
     9    100000      23686.0      0.2     63.3          do_stuff()
    10         1         22.0     22.0      0.1      print('Do something')
    11         1          2.0      2.0      0.0      print('Do something')
    12         1          1.0      1.0      0.0      print('Do something')
"""
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
