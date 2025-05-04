#!/usr/bin/env python3

""" Leetcode problem 2338: Count the Number of Ideal Arrays. """

from collections import Counter
import math


class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        result = maxValue
        frequency = {x: 1 for x in range(1, maxValue + 1)}
        for i in range(1, n):
            counter = Counter()
            for j in frequency:
                for k in range(2, maxValue // j + 1):
                    result += math.comb(n - 1, i) * frequency[j]
                    counter[k * j] += frequency[j]
            frequency = counter
            result %= 1_000_000_007
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
