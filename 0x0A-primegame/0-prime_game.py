#!/usr/bin/python3
"""0. Prime Game"""


def isWinner(x, nums):
    """
    Maria and Ben are playing a game.
    Given a set of consecutive integers starting from 1 up
    to and including n, they take turns choosing a prime
    number from the set and removing that number and its
    multiples from the set. The player that cannot make a
    move loses the game.

    They play x rounds of the game, where n may be different
    for each round. Assuming Maria always goes first and both
    players play optimally, determine who the winner of each
    game is.
    """
    ben = 0
    maria = 0

    def isPrime(n):
        """check is number is prime"""
        if n > 1:
            for i in range(2, (n // 2) + 1):
                if (n % i) == 0:
                    return False
            return True
        return True

    def arr(n):
        """make array"""
        nums = []
        for _ in range(1, n + 1):
            nums.append(_)
        return nums

    def sieve(n):
        """Generate all prime numbers up to n using a simple sieve."""
        nums = arr(n)
        primes = []
        for num in nums:
            if isPrime(num):
                primes.append(num)
        return primes
    turns = 0
    for n in nums:
        primes = sieve(n)
        if primes == []:
            ben += 1
        for i in primes:
            turns += 1
            primes.remove(i)
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
