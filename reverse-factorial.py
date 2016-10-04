import time
from math import factorial

factorials = {factorial(x):x for x in range(0, 20)}

def reverse_factorial_fast(num):
    if(num in factorials):
        return str(factorials[num]) + "!"
    else:
        return "NONE"

def reverse_factorial(num):
    if(num % 2 == 1):
        return "NONE"
    current_factor = 2.0;
    while num > 1:
        num /= current_factor
        if(num == 1):
            return str(int(current_factor)) + "!"
        elif(num < 1):
            return "NONE"

        current_factor += 1

challenge = [3628800, 479001600, 6, 18]

for x in range(1, 12):
    index = 1
    limit = factorial(x) + 1

    t_start = time.time()
    while(index < limit):
        reverse_factorial_fast(index)
        index += 1
    t_end = time.time()

    print "Time:", t_end - t_start
