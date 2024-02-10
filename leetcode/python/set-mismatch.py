#!/usr/bin/env python3

""" Leetcode problem 645: Set Mismatch. """

from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        table = set()
        for value in nums:
            if value in table:
                return [value, (n * (n + 1) // 2) - sum(nums) + value]
            table.add(value)
        return [0, 0]


def main() -> None:
    pass


if __name__ == "__main__":
    main()
