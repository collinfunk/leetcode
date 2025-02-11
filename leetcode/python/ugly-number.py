#!/usr/bin/env python3

""" Leetcode problem 263: Ugly Number. """


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 5 == 0:
            n /= 5
        while n % 3 == 0:
            n /= 3
        while n % 2 == 0:
            n /= 2
        return n == 1


def main() -> None:
    pass


if __name__ == "__main__":
    main()
