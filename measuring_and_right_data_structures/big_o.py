import random
import time

def double_first_amount(amount):
    return amount[0] * 2

def sum_odd_amount(amount):
    sum = 0
    for i in amount:
        if i % 2:
            sum += i
    return sum

randomamounts = [random.randint(1, 100) for _ in range(100000)]



start_time = time.time()
double_first_amount(randomamounts)
end_time = time.time()
double_time = end_time-start_time
print(double_time)

start_time = time.time()
sum_odd_amount(randomamounts)
end_time = time.time()
sum_time= end_time-start_time
print(sum_time)

print(double_time/sum_time)