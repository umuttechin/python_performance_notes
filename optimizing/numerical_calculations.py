"""
Numpy
    Unofficial standard for scientific computing
    Large ecosystem
    High performance
    Memory efficient

Pandas
    Relies on Numpy
    Data analysis and manipulation
    Tabular data(csv or from a relational database)
    High performance

---------------------------------

kernprof -lv numerical_calculations.py                                                                                                                                                                                      1 ↵
Wrote profile results to numerical_calculations.py.lprof
Timer unit: 1e-06 s

Total time: 1.16833 s
File: numerical_calculations.py
Function: main at line 28

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    28                                           @profile
    29                                           def main():
    30         1          0.0      0.0      0.0      SIZE = 1000000
    31         1    1051653.0    1e+06     90.0      orders = [random.randint(1, 100) for _ in range(SIZE)]
    32         1      89257.0  89257.0      7.6      loop_approach(orders)
    33         1      27421.0  27421.0      2.3      numpy_approach(orders)

"""
import random
import numpy as np

def loop_approach(orders):
    result = 0
    for order in orders:
        result += order * order
    return result


def numpy_approach(orders):
    numpy_orders = np.array(orders)
    return np.sum(numpy_orders * numpy_orders)

@profile
def main():
    SIZE = 1000000
    orders = [random.randint(1, 100) for _ in range(SIZE)]
    loop_approach(orders)
    numpy_approach(orders)
main()
