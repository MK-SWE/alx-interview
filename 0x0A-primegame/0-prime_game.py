#!/usr/bin/python3
"""
isWinner
determining the winner of a game based on the strategic
"""


def genPrimes(n: int):
    """Create a list of prime numbers
    Args:
        n (int): Number
    Returns:
        List[bool]: List of booleans
    """
    primes = [True for _ in range(n + 1)]
    primes[0] = primes[1] = False
    p = 2
    while p * p <= n:
        if primes[p] is True:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return primes


def isWinner(x: int, nums) -> str:
    """Prime Game
    Args:
        x (int): Number of rounds
        nums (List[int]): List of n
    Returns:
        str: Name of the player that won most rounds
    """

    def calculate_total(primes):
        """Calculate the total number of prime numbers
        Args:
            primes (List[bool]): List of prime numbers
        Returns:
            List[int]: List of total prime numbers
        """
        total = 0
        total_primes = []
        for i, is_prime in enumerate(primes):
            if is_prime is True:
                total += 1
            total_primes.append(total)
        return total_primes

    def can_win(total_primes, x: int) -> str:
        """Determine if the player can win the round
        Args:
            total_primes (List[int]): List of total prime numbers
            x (int): Number of rounds
        Returns:
            str: Name of the player that won most rounds
        """
        if sum(total != 0 for total in total_primes) == 0:
            return None
        if sum(total != 0 for total in total_primes) % 2 == 0:
            return "Maria"
        return "Ben"

    n = max(nums)
    primes = genPrimes(n)
    total_primes = calculate_total(primes)
    return can_win(total_primes, x)
