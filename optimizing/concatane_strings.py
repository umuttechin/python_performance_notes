"""
String concatanate
+ -> Strings are immutable, so recreating when modifying them
    Very friendly
    Scalable
    Slow performance

f - string
    High performance
    Friendly
    Not scalable

join()
    Less friendly
    Scalable
    High performance
"""

"""For generator are
    Lazy version of comprehensions
    Avoid upfront of full creation
    Just in time values
    Read lines from very large files
    Very low memory usage

Limitations
    Iterate only once
    No random cache
    Less flexible
    Access only next item

--------------------------------

kernprof -lv concatane_strings.py
Wrote profile results to concatane_strings.py.lprof
Timer unit: 1e-06 s

Total time: 0.065553 s
File: concatane_strings.py
Function: main at line 35

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    35                                           @profile
    36                                           def main():
    37         1      55415.0  55415.0     84.5      orders = [str(random.randint(1, 100)) for _ in range(50_000)]
    38         1          0.0      0.0      0.0      report = ""
    39     50001       4004.0      0.1      6.1      for o in orders:
    40     50000       5881.0      0.1      9.0          report += o
    41                                           
    42         1        253.0    253.0      0.4      "".join(orders)
    
--------------------------------

python -m memory_profiler concatane_strings.py                  
Filename: concatane_strings.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    35   20.125 MiB   20.125 MiB           1   @profile
    36                                         def main():
    37   23.547 MiB    3.422 MiB       50003       orders = [str(random.randint(1, 100)) for _ in range(50_000)]
    38   23.547 MiB    0.000 MiB           1       report = ""
    39   25.844 MiB    0.000 MiB       50001       for o in orders:
    40   25.844 MiB    2.297 MiB       50000           report += o
    41                                         
    42   25.844 MiB    0.000 MiB           1       "".join(orders)

"""
import random

@profile
def main():
    orders = [str(random.randint(1, 100)) for _ in range(50_000)]
    report = ""
    for o in orders:
        report += o

    "".join(orders)
    
main()
