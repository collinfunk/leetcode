#!/usr/bin/env python3

""" Leetcode problem 2413: Smallest Even Multiple. """


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if not (n / 2).is_integer():
            return n * 2
        return n


def main() -> None:
    pass


if __name__ == "__main__":
    main()
