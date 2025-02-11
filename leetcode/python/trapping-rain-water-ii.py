#!/usr/bin/env python3

""" Leetcode problem 407: Trapping Rain Water II. """

from typing import List
import heapq


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        m = len(heightMap)
        n = len(heightMap[0])
        if m < 3 or n < 3:
            return 0
        heap = []
        for i in range(0, m):
            for j in range(0, n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1
        level = 0
        result = 0
        while heap:
            height, x, y = heapq.heappop(heap)
            level = max(height, level)
            for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= i < m and 0 <= j < n and heightMap[i][j] != -1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    if heightMap[i][j] < level:
                        result += level - heightMap[i][j]
                    heightMap[i][j] = -1
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
