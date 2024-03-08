#!/usr/bin/env python3
from primelibpy import Prime as p
import sys

sys.set_int_max_str_digits(1000000)

primes = p.getPrimorialPrime(2,100)
print(primes)

for i in range(500000):
    for j in primes:
        primepow = str(pow(j,i))[:20]
        print(f"{j}^{i} = {primepow}...")
