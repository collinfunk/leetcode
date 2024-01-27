#!/usr/bin/env python3

""" Leetcode problem 326: Power of Three. """

import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n > 0:
            exponent = math.log(n, 3)
            value = round(exponent, 1)
            if math.pow(3, value) == n:
                return True
        return False


def main() -> None:
    pass


if __name__ == "__main__":
    main()
