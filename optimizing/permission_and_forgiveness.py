"""
Permission approach
    Check if operation will succeed, then proceed
    Use if statements

Forgiveness
    Handle problems after they happen
    Use try/except statements
    Prevent race condition bugs


If you expect rare bad data use forgiveness,
but if you expect high amount of bad data,
then use permission approach!
"""




import random


def permission(orders):
    result = []
    for amount in orders:
        if type(amount) == int:
            if amount > 50:
                result.append(2 * amount)
    return result

def forgiveness(orders):
    result = []
    for amount in orders:
        try:
            if amount > 50:
                result.append(2 * amount)
        except TypeError:
            pass
    return result
@profile
def main():
    orders = [random.randint(1, 100) for _ in range(100000)]

    for i in range(10):
        orders[i] = "bad data"

    permission(orders)
    forgiveness(orders)

    for i in range(100000):
        orders[i] = "bad data"

    permission(orders)
    forgiveness(orders)
main()
