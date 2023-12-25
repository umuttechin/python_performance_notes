"""Deques are;
 very fast - O(1) -
    fast append and pop at the end
    fast append and pop at the start
slow - O(n) -
    slow access by index

List are;
fast -
    slow access by index
    fast append and pop at the end
slow -
    slow append and pop at the start
"""

from collections import deque

@profile
def main():
    SIZE = 10000

    big_list = list(range(SIZE))
    big_deque = deque(big_list)

    while big_list:
        big_list.pop()
    while big_deque:
        big_deque.pop()

    big_list = list(range(SIZE))
    big_deque = deque(big_list)

    while big_list:
        big_list.pop(0)
    while big_deque:
        big_deque.popleft()








main()