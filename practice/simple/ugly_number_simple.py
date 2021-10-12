import time
def max_divide(a, b):
    while a% b == 0:
        a = a / b
    return a
# number whose only factors are 2, 3 or 5
def is_ugly_number(num):
    num = max_divide(num, 2)
    num = max_divide(num, 3)
    num = max_divide(num, 5)
    return True if num == 1 else False

def find_nth_ugly_number(n):
    index = 0
    nth_number = 0
    while index < n:
        nth_number += 1
        if is_ugly_number(nth_number):
            index += 1

    return nth_number

while True:
    try:
        n = int(input("Please enter the value of nth Ugly number: "))
        # n = 150
        start_time = time.time()
        print(n, "th ugly number is", find_nth_ugly_number(n))
        print("Duration:", time.time() - start_time)
    except:
        print("quit")
        break

