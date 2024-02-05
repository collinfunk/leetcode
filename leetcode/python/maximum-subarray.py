#!/usr/bin/env python3

""" Leetcode problem 53: Maximum Subarray. """

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = -inf
        current = 0
        for value in nums:
            current = max(value, current + value)
            best = max(best, current)
        return best


def main() -> None:
    pass


if __name__ == "__main__":
    main()
