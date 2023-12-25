"""
kernprof -lv risky_optimization.py
Wrote profile results to risky_optimization.py.lprof
Timer unit: 1e-06 s

Total time: 0.361297 s
File: risky_optimization.py
Function: main at line 10

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    10                                           @profile
    11                                           def main():
    12         2     310063.0 155031.5     85.8      orders = [(random.randint(1, 100),
    13                                                         random.randint(1, 100),
    14         1          1.0      1.0      0.0                random.randint(1, 100)) for _ in range(100_000)]
    15                                           
    16    100001       8582.0      0.1      2.4      for order in orders:
    17    100000      17530.0      0.2      4.9          multiple(order)
    18    100000      25121.0      0.3      7.0          individual(order)

"""

import random

def multiple(order):
    subtotal, tax, shipping = order

def individual(order):
    subtotal = order[0]
    tax = order[1]
    shipping = order[2]
@profile
def main():
    orders = [(random.randint(1, 100),
              random.randint(1, 100),
              random.randint(1, 100)) for _ in range(100_000)]

    for order in orders:
        multiple(order)
        individual(order)
main()

