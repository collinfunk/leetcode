#!/usr/bin/env python3

""" Leetcode problem 2364: Count Number of Bad Pairs. """

from collections import defaultdict


class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        result = 0
        table = defaultdict(int)
        for i in range(len(nums)):
            difference = i - nums[i]
            good_pairs = table[difference]
            result += i - good_pairs
            table[difference] = good_pairs + 1
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
