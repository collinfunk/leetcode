#!/usr/bin/env python3

""" Leetcode problem 2270: Number of Ways to Split Array. """

from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        valid = 0
        n = len(nums)
        for i in range(0, n - 1):
            left_sum += nums[i]
            right_sum -= nums[i]
            if right_sum <= left_sum:
                valid += 1
        return valid


def main() -> None:
    pass


if __name__ == "__main__":
    main()
