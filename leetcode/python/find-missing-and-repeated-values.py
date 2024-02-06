#!/usr/bin/env python3

""" Leetcode problem 2965: Find Missing and Repeated Values. """

from typing import List
from collections import defaultdict


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        count_map = defaultdict(int)
        a = 0
        b = 0
        for i in range(0, n):
            for j in range(0, n):
                count_map[grid[i][j]] += 1
        for i in range(1, (n * n) + 1):
            if count_map[i] == 2:
                a = i
            elif count_map[i] == 0:
                b = i
        return [a, b]


def main() -> None:
    pass


if __name__ == "__main__":
    main()
