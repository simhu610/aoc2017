import numpy as np
import math

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

a = np.arange(108100, 125100 + 1, 17)
foo = np.vectorize(is_prime)
pbools = foo(a)
primes = np.extract(pbools, a)
print primes
print len(a), len(primes), len(a) - len(primes)