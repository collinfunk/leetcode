#!/usr/bin/env python3

""" Leetcode problem 1267: Count Servers that Communicate. """

from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row_counts = [0] * len(grid[0])
        column_counts = [0] * len(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    column_counts[i] += 1
                    row_counts[j] += 1
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    if 1 < row_counts[j] or 1 < column_counts[i]:
                        result += 1
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
