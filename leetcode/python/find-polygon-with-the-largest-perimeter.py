#!/usr/bin/env python3

""" Leetcode problem 2971: Find Polygon With the Largest Perimeter. """

from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        side_sum = 0
        result = -1
        for i in range(0, len(nums)):
            if nums[i] < side_sum:
                result = nums[i] + side_sum
            side_sum += nums[i]
        return result


def main() -> None:
    var = [2, 4, 1, 3]
    var.sort()
    print(var)


if __name__ == "__main__":
    main()
