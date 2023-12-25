"""For generator are
    Lazy version of comprehensions
    Avoid upfront of full creation
    Just in time values
    Read lines from very large files
    Very low memory usage

Limitations
    Iterate only once
    No random cache
    Less flexible
    Access only next item

----------------------------

kernprof -lv generator.py                                                                                                                                                                                                 130 ↵
Wrote profile results to generator.py.lprof
Timer unit: 1e-06 s

Total time: 0.114526 s
File: generator.py
Function: main at line 19

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    19                                           @profile
    20                                           def main():
    21         1     101537.0 101537.0     88.7      orders = [random.randint(1, 100) for _ in range(100000)]
    22                                           
    23         1       5653.0   5653.0      4.9      comprehension = [2 * i for i in orders if i > 50 ]
    24         1          1.0      1.0      0.0      generator = (2 * i for i in orders if i > 50 )
    25                                           
    26                                           
    27         1        220.0    220.0      0.2      sum(comprehension)
    28         1       7115.0   7115.0      6.2      sum(generator)

----------------------------

python -m memory_profiler generator.py
Filename: generator.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    19   19.875 MiB   19.875 MiB           1   @profile
    20                                         def main():
    21   20.641 MiB    0.766 MiB      100003       orders = [random.randint(1, 100) for _ in range(100000)]
    22                                         
    23   20.891 MiB    0.250 MiB      100003       comprehension = [2 * i for i in orders if i > 50 ]
    24   20.906 MiB    0.016 MiB      149913       generator = (2 * i for i in orders if i > 50 )
    25                                         
    26                                         
    27   20.891 MiB    0.000 MiB           1       sum(comprehension)
    28   20.906 MiB    0.000 MiB           1       sum(generator)
    
"""
import random

def comprehension(orders):
    return [2 * i for i in orders if i > 50 ]

@profile
def main():
    orders = [random.randint(1, 100) for _ in range(100000)]

    comprehension = [2 * i for i in orders if i > 50 ]
    generator = (2 * i for i in orders if i > 50 )


    sum(comprehension)
    sum(generator)

main()

