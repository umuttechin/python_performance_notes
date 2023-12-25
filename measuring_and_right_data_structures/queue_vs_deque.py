"""Deques are;
 very fast - O(1) -
    fast append and pop at the end
    fast append and pop at the start
slow - O(n) -
    slow access by index

List are;
fast -
    slow access by index
    fast append and pop at the end
slow -
    slow append and pop at the start

----------------------------

 $ python -m memory_profiler queue_vs_deque.py                                                                                                                                                                               130 ↵
Filename: queue_vs_deque.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    18   19.062 MiB   19.062 MiB           1   @profile
    19                                         def main():
    20   19.062 MiB    0.000 MiB           1       SIZE = 10000
    21                                         
    22   19.344 MiB    0.281 MiB           1       big_list = list(range(SIZE))
    23   19.422 MiB    0.078 MiB           1       big_deque = deque(big_list)
    24                                         
    25   19.453 MiB    0.000 MiB       10001       while big_list:
    26   19.453 MiB    0.031 MiB       10000           big_list.pop()
    27   19.484 MiB    0.016 MiB       10001       while big_deque:
    28   19.484 MiB    0.016 MiB       10000           big_deque.pop()
    29                                         
    30   19.594 MiB    0.109 MiB           1       big_list = list(range(SIZE))
    31   19.656 MiB    0.062 MiB           1       big_deque = deque(big_list)
    32                                         
    33   19.656 MiB    0.000 MiB       10001       while big_list:
    34   19.656 MiB    0.000 MiB       10000           big_list.pop(0)
    35   19.672 MiB    0.016 MiB       10001       while big_deque:
    36   19.656 MiB    0.000 MiB       10000           big_deque.popleft()

---------------------------- 

 $ kernprof -lv queue_vs_deque.py             
Wrote profile results to queue_vs_deque.py.lprof
Timer unit: 1e-06 s

Total time: 0.013528 s
File: queue_vs_deque.py
Function: main at line 18

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    18                                           @profile
    19                                           def main():
    20         1          0.0      0.0      0.0      SIZE = 10000
    21                                           
    22         1         86.0     86.0      0.6      big_list = list(range(SIZE))
    23         1         84.0     84.0      0.6      big_deque = deque(big_list)
    24                                           
    25     10001        761.0      0.1      5.6      while big_list:
    26     10000       1055.0      0.1      7.8          big_list.pop()
    27     10001        757.0      0.1      5.6      while big_deque:
    28     10000       1058.0      0.1      7.8          big_deque.pop()
    29                                           
    30         1         96.0     96.0      0.7      big_list = list(range(SIZE))
    31         1         44.0     44.0      0.3      big_deque = deque(big_list)
    32                                           
    33     10001        821.0      0.1      6.1      while big_list:
    34     10000       6806.0      0.7     50.3          big_list.pop(0)
    35     10001        807.0      0.1      6.0      while big_deque:
    36     10000       1153.0      0.1      8.5          big_deque.popleft()
    
"""

from collections import deque

@profile
def main():
    SIZE = 10000

    big_list = list(range(SIZE))
    big_deque = deque(big_list)

    while big_list:
        big_list.pop()
    while big_deque:
        big_deque.pop()

    big_list = list(range(SIZE))
    big_deque = deque(big_list)

    while big_list:
        big_list.pop(0)
    while big_deque:
        big_deque.popleft()


main()
