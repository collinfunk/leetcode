#!/usr/bin/env python3

""" Leetcode problem 268: Missing Number. """

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        table = set(nums)
        for i in range(0, length + 1):
            if i not in table:
                return i
        # Unreachable.
        return -1


def main() -> None:
    pass


if __name__ == "__main__":
    main()
