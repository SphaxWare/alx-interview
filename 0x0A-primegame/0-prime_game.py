#!/usr/bin/python3
"""0. Prime Game"""


def isWinner(x, nums):
    """winner winner chicken dinner"""
    ben = 0
    maria = 0

    def isPrime(n):
        """Check if a number is prime"""
        if n == 1:
            return False
        if n > 1:
            for i in range(2, (n // 2) + 1):
                if (n % i) == 0:
                    return False
            return True
        return True

    def sieve(n):
        """Generate all prime numbers up to n using a simple sieve."""
        primes = []
        for num in range(2, n):
            if isPrime(num):
                primes.append(num)
        return primes

    def removemul(prime, arr):
        """remove prime and its mutiples"""
        for n in arr:
            if n % prime == 0:
                arr.remove(n)
        return arr

    for j in range(x):
        roundset = list(range(1, nums[j] + 1))
        primes = sieve(nums[j] + 1)
        if primes == []:
            ben += 1
            continue

        if len(nums) == 1 and isPrime(nums[0]):
            maria += 1

        turns = 0
        for i in primes:
            turns += 1
            roundset = removemul(i, roundset)

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
