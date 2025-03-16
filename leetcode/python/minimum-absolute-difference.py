#!/usr/bin/env python3

""" Leetcode problem 1200. Minimum Absolute Difference. """

from collections import defaultdict


class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        table = defaultdict(list)
        min_diff = float('inf')
        arr.sort()
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            table[diff].append([arr[i], arr[i + 1]])
            min_diff = min(min_diff, diff)
        return table[min_diff]


def main() -> None:
    pass


if __name__ == "__main__":
    main()
