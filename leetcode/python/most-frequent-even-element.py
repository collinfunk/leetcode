#!/usr/bin/env python3

""" Leetcode problem 2404: Most Frequent Even Element. """

from typing import List
from math import inf


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        table = dict()
        max_count = -inf
        for value in nums:
            if (value % 2) == 0:
                table[value] = table.get(value, 0) + 1
        for value, count in table.items():
            if count >= max_count:
                if count > max_count:
                    max_count = count
                    result = value
                else:
                    result = min(value, result)
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
