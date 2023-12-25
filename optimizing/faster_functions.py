"""
Self - sufficient functions
    Duplicate code
    Less reusable
    More difficult to maintain
    Better performance

Calling other functions
    Clean code
    More reusable
    Easier to maintain
    Slower performance(overhead of calling many times)

------------------------------------------------------------------
kernprof -lv faster_functions.py
Wrote profile results to faster_functions.py.lprof
Timer unit: 1e-06 s

Total time: 0.00013 s
File: faster_functions.py
Function: main at line 21

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    21                                           @profile
    22                                           def main():
    23         1          1.0      1.0      0.8      SIZE = 25
    24         1         36.0     36.0     27.7      [random.randint(1, 100) for _ in range(SIZE)]
    25         1         30.0     30.0     23.1      [get_random() for _ in range(SIZE)]
    26         1         31.0     31.0     23.8      [(lambda: random.randint(0, 100))() for _ in range(SIZE)]
    27         1         32.0     32.0     24.6      [(lambda: get_random())() for _ in range(SIZE)]

"""

import random

def get_random():
    return random.randint(0 , 100)

@profile
def main():
    SIZE = 25
    [random.randint(1, 100) for _ in range(SIZE)]
    [get_random() for _ in range(SIZE)]
    [(lambda: random.randint(0, 100))() for _ in range(SIZE)]
    [(lambda: get_random())() for _ in range(SIZE)]
    
main()
