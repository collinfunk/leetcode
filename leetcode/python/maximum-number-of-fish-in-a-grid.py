#!/usr/bin/env python3

""" Leetcode problem 2658: Maximum Number of Fish in a Grid. """


class Solution:
    def findMaxFish(self, grid: list[list[int]]) -> int:
        def dfs(i: int, j: int) -> int:
            count = grid[i][j]
            grid[i][j] = 0
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] != 0:
                    count += dfs(ni, nj)
            return count
        m = len(grid)
        n = len(grid[0])
        max_fish = 0
        for i in range(m):
            for j in range(n):
                if 0 < grid[i][j]:
                    max_fish = max(max_fish, dfs(i, j))
        return max_fish


def main() -> None:
    pass


if __name__ == "__main__":
    main()
