#!/usr/bin/env python3

""" Leetcode problem 1929: Concatenation of Array. """

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return [*nums, *nums]


def main() -> None:
    pass


if __name__ == "__main__":
    main()
