#!/usr/bin/env python3

""" Leetcode problem 1765: Map of Highest Peak. """

from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        height = [[float('inf')] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                else:
                    if 0 < i:
                        height[i][j] = min(height[i][j], height[i - 1][j] + 1)
                    if 0 < j:
                        height[i][j] = min(height[i][j], height[i][j - 1] + 1)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i < m - 1:
                    height[i][j] = min(height[i][j], height[i + 1][j] + 1)
                if j < n - 1:
                    height[i][j] = min(height[i][j], height[i][j + 1] + 1)
        return height


def main() -> None:
    pass


if __name__ == "__main__":
    main()
