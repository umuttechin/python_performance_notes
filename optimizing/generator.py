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
"""
import random

def comprehension(orders):
    return [2 * i for i in orders if i > 50 ]

@profile
def main():
    orders = [random.randint(1, 100) for _ in range(100000)]

    comprehension = [2 * i for i in orders if i > 50 ]
    generator = (2 * i for i in orders if i > 50 )


    sum(comprehension)
    sum(generator)

main()

