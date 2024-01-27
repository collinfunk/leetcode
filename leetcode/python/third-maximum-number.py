#!/usr/bin/env python3

""" Leetcode problem 414: Third Maximum Number. """

from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(list(set(nums))) < 3:
            return max(list(set(nums)))
        else:
            return sorted(list(set(nums)))[-3]


def main() -> None:
    pass


if __name__ == "__main__":
    main()
