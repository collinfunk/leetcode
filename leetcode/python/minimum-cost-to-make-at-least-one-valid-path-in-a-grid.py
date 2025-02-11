#!/usr/bin/env python3

""" Leetcode problem 1368: Minimum Cost to Make at Least One Valid Path in a Grid. """

from typing import List
import heapq


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        pq = [(0, 0, 0)]
        visited = set()
        while pq:
            cost, row, column = heapq.heappop(pq)
            if (row, column) == (rows - 1, columns - 1):
                return cost
            if (row, column) in visited:
                continue
            visited.add((row, column))
            for i, (dr, dc) in enumerate(directions, 1):
                nr = row + dr
                nc = column + dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= columns or (nr, nc) in visited:
                    continue
                if i == grid[row][column]:
                    heapq.heappush(pq, (cost, nr, nc))
                else:
                    heapq.heappush(pq, (cost + 1, nr, nc))


def main() -> None:
    pass


if __name__ == "__main__":
    main()
