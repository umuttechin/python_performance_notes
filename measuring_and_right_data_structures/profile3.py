"""
pip install memory_profiler

 $ python -m memory_profiler profile3.py
Filename: profile3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     1   18.828 MiB   18.828 MiB           1   @profile
     2                                         def create_big_list():
     3   95.141 MiB   76.312 MiB           1       return 10_000_000 * [0]


Filename: profile3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     6   95.141 MiB   95.141 MiB           1   @profile
     7                                         def create_huge_list():
     8  324.031 MiB  228.891 MiB           1       return 30_000_000 * [0]

"""
@profile
def create_big_list():
    return 10_000_000 * [0]


@profile
def create_huge_list():
    return 30_000_000 * [0]


create_big_list()
create_huge_list()
