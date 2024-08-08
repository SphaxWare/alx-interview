#!/usr/bin/python3
"""0. Prime Game"""


def isWinner(x, nums):
    ben = 0
    maria = 0

    def isPrime(n):
        """Check if a number is prime"""
        if n > 1:
            for i in range(2, (n // 2) + 1):
                if (n % i) == 0:
                    return False
            return True
        return True

    def sieve(n):
        """Generate all prime numbers up to n using a simple sieve."""
        primes = []
        for num in range(1, n):
            if isPrime(num):
                primes.append(num)
        return primes

    for j in range(x):
        roundset = list(range(1, nums[j] + 1))
        primes = sieve(nums[j])
        if not primes:
            ben += 1
            continue

        turns = 0
        while primes:
            current_prime = primes.pop(0)
            turns += 1
            roundset = [num for num in roundset if num % current_prime != 0]
            primes = [p for p in primes if p in roundset]

        if turns % 2 == 0:
            ben += 1
        else:
            maria += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
