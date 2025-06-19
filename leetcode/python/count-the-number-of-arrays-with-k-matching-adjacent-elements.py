#!/usr/bin/env python3

""" Leetcode problem 3405: Count the Number of Arrays with K Matching Adjacent Elements. """

import math


class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        mod = (10 ** 9) + 7
        return m * pow(m - 1, n - k - 1, mod) * math.comb(n - 1, k) % mod


def main() -> None:
    pass


if __name__ == "__main__":
    main()
