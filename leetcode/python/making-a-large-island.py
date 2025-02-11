#!/usr/bin/env python3

""" Leetcode problem 827: Making A Large Island. """

from collections import defaultdict, deque


class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        def visit(start: tuple[int, int]) -> None:
            queue = deque([start])
            water = set()
            area = 1
            while queue:
                i, j = queue.pop()
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < n and 0 <= nj < m:
                        if grid[ni][nj] == 1:
                            grid[ni][nj] = -1
                            queue.append((ni, nj))
                            area += 1
                        elif grid[ni][nj] == 0:
                            water.add((ni, nj))
            for cell in water:
                water_area[cell] += area
        n = len(grid)
        m = len(grid[0])
        water_area = defaultdict(int)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    grid[i][j] = -1
                    visit((i, j))
        if water_area:
            return max(water_area.values()) + 1
        if grid[0][0] == 0:
            return 1
        return n * m


def main() -> None:
    pass


if __name__ == "__main__":
    main()
