"""Dictionaries are;
very fast - O(1) -
    getting
    setting
    deleting
slow - O(n) -
    worst cases

-------------------------

 $ python -m memory_profiler dictionary.py
Filename: dictionary.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    26   19.109 MiB   19.109 MiB           1   @profile
    27                                         def main():
    28   19.109 MiB    0.000 MiB           1       SIZE = 100000
    29   19.109 MiB    0.000 MiB           1       big_list = []
    30   19.109 MiB    0.000 MiB           1       big_dictionary = {}
    31                                         
    32   62.359 MiB    0.047 MiB      100001       for i in range(SIZE):
    33   62.359 MiB   25.469 MiB      100000           big_list.append([i, i * 2, i * i])
    34   62.359 MiB   17.734 MiB      100000           big_dictionary[i] = [i * 2, i * i]
    35                                         
    36   62.391 MiB    0.031 MiB        1003       order_2_search = [random.randint(0, SIZE) for _ in range(1000)]
    37                                         
    38   62.391 MiB    0.000 MiB           1       search_list(big_list, order_2_search)
    39   62.391 MiB    0.000 MiB           1       search_dict(big_dictionary, order_2_search)

-------------------------

 $ kernprof -lv dictionary.py
Wrote profile results to dictionary.py.lprof
Timer unit: 1e-06 s

Total time: 7.06769 s
File: dictionary.py
Function: main at line 26

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    26                                           @profile
    27                                           def main():
    28         1          0.0      0.0      0.0      SIZE = 100000
    29         1          0.0      0.0      0.0      big_list = []
    30         1          0.0      0.0      0.0      big_dictionary = {}
    31                                           
    32    100001       8597.0      0.1      0.1      for i in range(SIZE):
    33    100000      38795.0      0.4      0.5          big_list.append([i, i * 2, i * i])
    34    100000      16672.0      0.2      0.2          big_dictionary[i] = [i * 2, i * i]
    35                                           
    36         1       1066.0   1066.0      0.0      order_2_search = [random.randint(0, SIZE) for _ in range(1000)]
    37                                           
    38         1    7002178.0    7e+06     99.1      search_list(big_list, order_2_search)
    39         1        383.0    383.0      0.0      search_dict(big_dictionary, order_2_search)
    
"""
import random

def search_list(big_list, items):
    counter = 0
    for i in items:
        for j in big_list:
            if i == j[0]:
                counter += 1
    return counter

def search_dict(big_dict, items):
    counter = 0
    for i in items:
        if i in big_dict:
            counter += 1
    return counter

@profile
def main():
    SIZE = 100000
    big_list = []
    big_dictionary = {}

    for i in range(SIZE):
        big_list.append([i, i * 2, i * i])
        big_dictionary[i] = [i * 2, i * i]

    order_2_search = [random.randint(0, SIZE) for _ in range(1000)]

    search_list(big_list, order_2_search)
    search_dict(big_dictionary, order_2_search)

main()
