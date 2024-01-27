#!/usr/bin/env python3

""" Leetcode problem 463: Island Perimeter. """

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        perimeter = 0
        for i in range(0, rows):
            for j in range(0, columns):
                if grid[i][j] == 1:
                    current_perimeter = 4
                    if i > 0 and grid[i - 1][j] == 1:
                        current_perimeter -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        current_perimeter -= 2
                    perimeter += current_perimeter
        return perimeter


def main() -> None:
    pass


if __name__ == "__main__":
    main()
