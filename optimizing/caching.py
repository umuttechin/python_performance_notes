"""Caching limitations
    Extra memory
    no side effect
    old data

How to use
    Basic approach with dictionaries
    Use @lru_cache()
    Thir party module(joblib) use also disk not only memory

------------------------- without lru_cache

kernprof -lv caching.py
Wrote profile results to caching.py.lprof
Timer unit: 1e-06 s

Total time: 4.25491 s
File: caching.py
Function: main at line 29

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    29                                           @profile
    30                                           def main():
    31         1       1045.0   1045.0      0.0      orders_2_search = [random.randint(1, 100) for _ in range(1000)]
    32      1001        147.0      0.1      0.0      for order in orders_2_search:
    33      1000    4253716.0   4253.7    100.0          get_order_details(order)

------------------------- with lru_cache(10x better)

kernprof -lv caching.py
Wrote profile results to caching.py.lprof
Timer unit: 1e-06 s

Total time: 0.444047 s
File: caching.py
Function: main at line 29

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    29                                           @profile
    30                                           def main():
    31         1       1207.0   1207.0      0.3      orders_2_search = [random.randint(1, 100) for _ in range(1000)]
    32      1001         95.0      0.1      0.0      for order in orders_2_search:
    33      1000     442745.0    442.7     99.7          get_order_details(order)

    
"""
import random

"""A basic approach for caching:
cache = {}
def heavy_calculation(order_id):
    if order_id not in cache:
        do_heavy_work
        
        cache[order_id] = ...
    return cache[order_id]
"""
from  functools import lru_cache
@lru_cache
def get_order_details(order_id):
    for i in range(100_000):
        pass
    return 1200 * order_id

@profile
def main():
    orders_2_search = [random.randint(1, 100) for _ in range(1000)]
    for order in orders_2_search:
        get_order_details(order)

main()
