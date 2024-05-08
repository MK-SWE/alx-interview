#!/usr/bin/env python3
"""
Count the minimum steps to the solution
"""
from typing import List


def minOperations(n: int) -> int:
    """Return the sum of the prime factors"""
    if n <= 0:
        return 0
    # A list to collect the prime factors
    factors = []
    # First, get the number of 2s that divide n
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # Now, n must be odd at this point
    #so we can skip one element (Note i = i + 2)
    for i in range(3, int(n**0.5) + 1, 2):
        # While i divides n, append i and divide n
        while n % i == 0:
            factors.append(i)
            n //= i
    # If n is a prime number greater than 2, then append n
    if n > 2:
        factors.append(n)
    return sum(factors)
