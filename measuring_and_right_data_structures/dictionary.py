"""Dictionaries are;
very fast - O(1) -
    getting
    setting
    deleting
slow - O(n) -
    worst cases
"""
import random

def search_list(big_list, items):
    counter = 0
    for i in items:
        for j in big_list:
            if i == j[0]:
                counter += 1
    return counter

def search_dict(big_dict, items):
    counter = 0
    for i in items:
        if i in big_dict:
            counter += 1
    return counter

@profile
def main():
    SIZE = 100000
    big_list = []
    big_dictionary = {}

    for i in range(SIZE):
        big_list.append([i, i * 2, i * i])
        big_dictionary[i] = [i * 2, i * i]

    order_2_search = [random.randint(0, SIZE) for _ in range(1000)]

    search_list(big_list, order_2_search)
    search_dict(big_dictionary, order_2_search)






main()