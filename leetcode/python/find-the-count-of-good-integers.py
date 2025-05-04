#!/usr/bin/env python3

""" Leetcode problem 3272: Find the Count of Good Integers. """

import math


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        table = set()
        base = 10 ** ((n - 1) // 2)
        skip = n & 1
        for i in range(base, base * 10):
            s = str(i)
            s += s[::-1][skip:]
            palindromic_integer = int(s)
            if palindromic_integer % k == 0:
                s = ''.join(sorted(s))
                table.add(s)
        factorials = [math.factorial(i) for i in range(n + 1)]
        result = 0
        for s in table:
            count = [0] * 10
            for c in s:
                count[int(c)] += 1
            total = (n - count[0]) * factorials[n - 1]
            for x in count:
                total //= factorials[x]
            result += total
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
