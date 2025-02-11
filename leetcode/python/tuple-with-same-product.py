#!/usr/bin/env python3

""" Leetcode problem 1726: Tuple with Same Product. """

from collections import defaultdict


class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        table = defaultdict(int)
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                table[nums[i] * nums[j]] += 1
        result = 0
        for value in table.values():
            if 1 < value:
                result += value * (value - 1) * 4
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
