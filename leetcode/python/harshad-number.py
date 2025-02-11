#!/usr/bin/env python3

""" Leetcode problem 3099: Harshad Number. """


class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        divisor = sum([int(digit) for digit in str(x)])
        if x % divisor == 0:
            return divisor
        else:
            return -1


def main() -> None:
    pass


if __name__ == "__main__":
    main()
