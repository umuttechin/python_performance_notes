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