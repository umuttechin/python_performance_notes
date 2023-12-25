import random

def multiple(order):
    subtotal, tax, shipping = order

def individual(order):
    subtotal = order[0]
    tax = order[1]
    shipping = order[2]
@profile
def main():
    orders = [(random.randint(1, 100),
              random.randint(1, 100),
              random.randint(1, 100)) for _ in range(100_000)]

    for order in orders:
        multiple(order)
        individual(order)
main()

