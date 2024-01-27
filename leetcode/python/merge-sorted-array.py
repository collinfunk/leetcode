#!/usr/bin/env python3

""" Leetcode problem 88: Merge Sorted Array. """

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) \
            -> None:
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()


def main() -> None:
    pass


if __name__ == "__main__":
    main()
