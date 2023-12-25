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

