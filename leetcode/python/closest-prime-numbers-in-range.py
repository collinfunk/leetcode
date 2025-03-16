#!/usr/bin/env python3

""" Leetcode problem 2523: Closest Prime Numbers in Range. """


class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        def is_prime(value: int) -> bool:
            if value <= 1:
                return False
            if value == 2 or value == 3:
                return True
            if value % 2 == 0 or value % 3 == 0:
                return False
            i = 5
            while i * i <= value:
                if value % i == 0 or value % (i + 2) == 0:
                    return False
                i += 6
            return True
        primes = []
        for candidate in range(left, right + 1):
            if is_prime(candidate):
                if primes and candidate <= primes[-1] + 2:
                    return [primes[-1], candidate]
                primes.append(candidate)
        gaps = ([primes[i - 1], primes[i]] for i in range(1, len(primes)))
        return min(gaps, key=lambda gap: (gap[1] - gap[0], gap[0]), default=[-1, -1])


def main() -> None:
    pass


if __name__ == "__main__":
    main()
