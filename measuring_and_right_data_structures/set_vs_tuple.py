"""Sets are;
 very fast - O(1) -
    adding
    deleting
    membership checking
slow - O(n) -
    removing duplicates

Tuples are;
    memory efficient
    fixed content

----------------------------

python -m memory_profiler set_vs_tuple.py
Filename: set_vs_tuple.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    23   20.312 MiB   20.312 MiB           1   @profile
    24                                         def main():
    25   20.312 MiB    0.000 MiB           1       SIZE = 1_000_000
    26                                         
    27   58.938 MiB   38.625 MiB           1       big_list = list(range(SIZE))
    28  121.625 MiB   62.688 MiB           1       big_set = set(big_list)
    29  129.297 MiB    7.672 MiB           1       big_tuple = tuple(big_list)
    30                                         
    31  129.391 MiB    0.094 MiB        1003       item_2_find = [random.randint(1, SIZE) for _ in range(1000)]
    32                                         
    33  129.391 MiB    0.000 MiB           1       search(item_2_find, big_list)
    34  129.391 MiB    0.000 MiB           1       search(item_2_find, big_set)
    35  129.406 MiB    0.016 MiB           1       search(item_2_find, big_tuple)
    
----------------------------

kernprof -lv set_vs_tuple.py                                                                                                                                                                                             
Wrote profile results to set_vs_tuple.py.lprof
Timer unit: 1e-06 s

Total time: 6.50834 s
File: set_vs_tuple.py
Function: main at line 23

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    23                                           @profile
    24                                           def main():
    25         1          1.0      1.0      0.0      SIZE = 1_000_000
    26                                           
    27         1      10791.0  10791.0      0.2      big_list = list(range(SIZE))
    28         1      15609.0  15609.0      0.2      big_set = set(big_list)
    29         1       2001.0   2001.0      0.0      big_tuple = tuple(big_list)
    30                                           
    31         1       1171.0   1171.0      0.0      item_2_find = [random.randint(1, SIZE) for _ in range(1000)]
    32                                           
    33         1    3325845.0    3e+06     51.1      search(item_2_find, big_list)
    34         1        314.0    314.0      0.0      search(item_2_find, big_set)
    35         1    3152608.0    3e+06     48.4      search(item_2_find, big_tuple)

"""
import random


def search(items, collection):
    count = 0
    for i in items:
        if i in collection:
            count += 1
    return count

@profile
def main():
    SIZE = 1_000_000

    big_list = list(range(SIZE))
    big_set = set(big_list)
    big_tuple = tuple(big_list)

    item_2_find = [random.randint(1, SIZE) for _ in range(1000)]

    search(item_2_find, big_list)
    search(item_2_find, big_set)
    search(item_2_find, big_tuple)

main()
