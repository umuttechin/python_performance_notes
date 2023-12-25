"""Sets are;
 very fast - O(1) -
    adding
    deleting
    membership checking
slow - O(n) -
    removing duplicates

Tuples are;
    memory efficient
    fixed content
"""
import random


def search(items, collection):
    count = 0
    for i in items:
        if i in collection:
            count += 1
    return count

@profile
def main():
    SIZE = 1_000_000

    big_list = list(range(SIZE))
    big_set = set(big_list)
    big_tuple = tuple(big_list)

    item_2_find = [random.randint(1, SIZE) for _ in range(1000)]

    search(item_2_find, big_list)
    search(item_2_find, big_set)
    search(item_2_find, big_tuple)

main()