"""For loops are
    more flexible
    better for adding more logic
    lenghty
    Slower for simple logic

List comprehension are
    only for creating a new list
    great for simple logic
    concise
    faster for simple logic
    set and dictionary comprehensions

----------------------------

kernprof -lv for_vs_collections.py
Wrote profile results to for_vs_collections.py.lprof
Timer unit: 1e-06 s

Total time: 0.114319 s
File: for_vs_collections.py
Function: main at line 28

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    28                                           @profile
    29                                           def main():
    30         1      98962.0  98962.0     86.6      orders = [random.randint(1, 100) for _ in range(100000)]
    31                                           
    32         1       9926.0   9926.0      8.7      loop(orders)
    33         1       5431.0   5431.0      4.8      comprehension(orders)
    
"""
import random


def loop(orders):
    result = []
    for amount in orders:
        if amount > 50:
            result.append(2 * amount)

    return result

def comprehension(orders):
    return [2 * i for i in orders if i > 50 ]

@profile
def main():
    orders = [random.randint(1, 100) for _ in range(100000)]

    loop(orders)
    comprehension(orders)

main()
