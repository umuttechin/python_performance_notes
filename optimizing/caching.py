"""Caching limitations
    Extra memory
    no side effect
    old data

How to use
    Basic approach with dictionaries
    Use @lru_cache()
    Thir party module(joblib) use also disk not only memory
"""
import random

"""A basic approach for caching:
cache = {}
def heavy_calculation(order_id):
    if order_id not in cache:
        do_heavy_work
        
        cache[order_id] = ...
    return cache[order_id]
"""
from  functools import lru_cache
@lru_cache
def get_order_details(order_id):
    for i in range(100_000):
        pass
    return 1200 * order_id

@profile
def main():
    orders_2_search = [random.randint(1, 100) for _ in range(1000)]
    for order in orders_2_search:
        get_order_details(order)

main()