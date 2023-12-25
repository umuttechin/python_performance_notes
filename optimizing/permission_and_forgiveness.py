"""
Permission approach
    Check if operation will succeed, then proceed
    Use if statements

Forgiveness
    Handle problems after they happen
    Use try/except statements
    Prevent race condition bugs

If you expect rare bad data use forgiveness,
but if you expect high amount of bad data,
then use permission approach!

--------------------------------------------------------------
kernprof -lv permission_and_forgiveness.py
Wrote profile results to permission_and_forgiveness.py.lprof
Timer unit: 1e-06 s

Total time: 0.195078 s
File: permission_and_forgiveness.py
Function: main at line 35

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    35                                           @profile
    36                                           def main():
    37         1      99145.0  99145.0     50.8      orders = [random.randint(1, 100) for _ in range(100000)]
    38                                           
    39        11          3.0      0.3      0.0      for i in range(10):
    40        10          2.0      0.2      0.0          orders[i] = "bad data"
    41                                           
    42         1      17546.0  17546.0      9.0      permission(orders)
    43         1      12813.0  12813.0      6.6      forgiveness(orders)
    44                                           
    45    100001       7857.0      0.1      4.0      for i in range(100000):
    46    100000       8447.0      0.1      4.3          orders[i] = "bad data"
    47                                           
    48         1       9835.0   9835.0      5.0      permission(orders)
    49         1      39430.0  39430.0     20.2      forgiveness(orders)

"""

import random


def permission(orders):
    result = []
    for amount in orders:
        if type(amount) == int:
            if amount > 50:
                result.append(2 * amount)
    return result

def forgiveness(orders):
    result = []
    for amount in orders:
        try:
            if amount > 50:
                result.append(2 * amount)
        except TypeError:
            pass
    return result
@profile
def main():
    orders = [random.randint(1, 100) for _ in range(100000)]

    for i in range(10):
        orders[i] = "bad data"

    permission(orders)
    forgiveness(orders)

    for i in range(100000):
        orders[i] = "bad data"

    permission(orders)
    forgiveness(orders)

main()
