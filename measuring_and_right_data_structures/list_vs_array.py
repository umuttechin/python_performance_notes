"""List are;
 very fast - O(1) -
    getting
    setting
    appending new items
slow - O(n) -
    finding
    removing items
memory allocation
    extra room for future appends
    old list is copied to the new list
"""

import numpy


def double_list(size):
    initial_list = list(range(size))
    return [i * 2 for i in initial_list]

def double_numpy(size):
    initial_array = numpy.arange(size)
    return list(2 * initial_array)

(double_list(10))
(double_numpy(10))
