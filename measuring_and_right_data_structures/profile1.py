"""
python profile1.py                                                                                                                                                                                                        
0.0059010982513427734

------------------------------

python -m profile profile1.py
0.2814948558807373  100008 function calls in 0.098 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.094    0.094 :0(exec)
        1    0.000    0.000    0.000    0.000 :0(print)
        1    0.005    0.005    0.005    0.005 :0(setprofile)
        2    0.000    0.000    0.000    0.000 :0(time)
        1    0.000    0.000    0.094    0.094 profile1.py:1(<module>)
        1    0.050    0.050    0.093    0.093 profile1.py:3(heavy_work)
   100000    0.043    0.000    0.043    0.000 profile1.py:7(do_stuff)
        1    0.000    0.000    0.098    0.098 profile:0(<code object <module> at 0x104c0e710, file "profile1.py", line 1>)
        0    0.000             0.000          profile:0(profiler)
------------------------------
python -m cProfile profile1.py                                                                                                                                                                                         
0.009616851806640625 100007 function calls in 0.010 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.010    0.010 profile1.py:1(<module>)
        1    0.007    0.007    0.010    0.010 profile1.py:3(heavy_work)
   100000    0.003    0.000    0.003    0.000 profile1.py:7(do_stuff)
        1    0.000    0.000    0.010    0.010 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        2    0.000    0.000    0.000    0.000 {built-in method time.time}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

      
"""
import time

def heavy_work():
    for _ in range(100_000):
        do_stuff()

def do_stuff():
    return 1 + 2

start_time = time.time()
heavy_work()
end_time = time.time()

print(end_time-start_time)
