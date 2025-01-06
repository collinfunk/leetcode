#!/usr/bin/env python3

""" Leetcode problem 724: Find Pivot Index. """

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sum = sum(nums)
        left_sum = 0
        n = len(nums)
        for i in range(0, n):
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1


def main() -> None:
    pass


if __name__ == "__main__":
    main()
