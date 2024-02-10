#!/usr/bin/env python3

""" Leetcode problem 2239: Find Closest Number to Zero. """

from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        result = nums[0]
        for value in nums[1:]:
            if abs(result) == abs(value):
                if value > result:
                    result = value
            elif abs(result) > abs(value):
                result = value
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
