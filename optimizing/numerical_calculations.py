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
