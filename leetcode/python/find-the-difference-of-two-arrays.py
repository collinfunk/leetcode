#!/usr/bin/env python3

""" Leetcode problem 2215: Find the Difference of Two Arrays. """

from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        table1 = set(nums1)
        table2 = set(nums2)
        result1 = [x for x in table1 if x not in table2]
        result2 = [x for x in table2 if x not in table1]
        return [result1, result2]


def main() -> None:
    pass


if __name__ == "__main__":
    main()
