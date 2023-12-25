"""For loops are
    more flexible
    better for adding more logic
    lenghty
    Slower for simple logic

List comprehension are
    only for creating a new list
    great for simple logic
    concise
    faster for simple logic
    set and dictionary comprehensions
"""
import random


def loop(orders):
    result = []
    for amount in orders:
        if amount > 50:
            result.append(2 * amount)

    return result

def comprehension(orders):
    return [2 * i for i in orders if i > 50 ]

@profile
def main():
    orders = [random.randint(1, 100) for _ in range(100000)]

    loop(orders)
    comprehension(orders)

main()

