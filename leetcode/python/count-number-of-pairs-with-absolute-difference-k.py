#!/usr/bin/env python3

""" Leetcode problem 2006: Count Number of Pairs With Absolute Difference K. """

from collections import defaultdict


class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        seen = defaultdict(int)
        result = 0
        for num in nums:
            result += seen[num - k] + seen[num + k]
            seen[num] += 1
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
