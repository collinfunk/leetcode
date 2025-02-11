#!/usr/bin/env python3

""" Leetcode problem 228: Summary Ranges. """

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        for num in nums:
            if ranges and ranges[-1][1] == num - 1:
                ranges[-1][1] = num
            else:
                ranges.append((num, num))


def main() -> None:
    pass


if __name__ == "__main__":
    main()
