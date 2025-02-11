#!/usr/bin/env python3

""" Leetcode problem 2017: Grid Game. """

from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        first = sum(grid[0])
        second = 0
        minimum = float("inf")
        for i in range(len(grid[0])):
            first -= grid[0][i]
            minimum = min(minimum, max(first, second))
            second += grid[1][i]
        return minimum


def main() -> None:
    pass


if __name__ == "__main__":
    main()
