import math
def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False

# Get the next after a given number
def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        # Next call to the function will continue here!   
        number += 1 

# Get the sum of all prime numbers under a number
def sum_primes_under(limit):
    total = 2
    for next_prime in get_primes(3):
        if next_prime < limit:
            total += next_prime
        else:
            print(total)
            return
print(sum_primes_under(2000000))    