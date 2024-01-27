#!/usr/bin/env python3

""" Leetcode problem 169: Majority Element. """

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_nums = len(nums) // 2
        counts = dict()

        for num in nums:
            if not counts.get(num):
                counts[num] = 1
            else:
                counts[num] = counts[num] + 1
                if counts[num] > max_nums:
                    return num
        return nums[0]


def main() -> None:
    pass


if __name__ == "__main__":
    main()
