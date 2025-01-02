#!/usr/bin/env python3

""" Leetcode problem 448: Find All Numbers Disappeared in an Array"""

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        table = set(nums)
        result = []

        for i in range(1, len(nums) + 1):
            if i not in table:
                result.append(i)

        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
