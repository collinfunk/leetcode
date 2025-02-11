#!/usr/bin/env python3

""" Leetcode problem 1920: Build Array from Permutation. """

from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        for i in range(0, len(nums)):
            result[i] = nums[nums[i]]
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
