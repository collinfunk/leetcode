#!/usr/bin/env python3

""" Leetcode problem 2503: Maximum Number of Points From Grid Queries. """

from queue import PriorityQueue


class Solution:
    def maxPoints(self, grid: list[list[int]], queries: list[int]) -> list[int]:
        m = len(grid)
        n = len(grid[0])
        k = len(queries)
        queue = PriorityQueue()
        queue.put((grid[0][0], 0, 0))
        visited = 0
        threshold = [0] * ((m * n) + 1)
        min_value = [[float("inf")] * n for _ in range(m)]
        min_value[0][0] = grid[0][0]
        while not queue.empty():
            current = queue.get()
            threshold[visited + 1] = current[0]
            visited += 1
            for direction in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                new_row = current[1] + direction[0]
                new_column = current[2] + direction[1]
                if 0 <= new_row < m and 0 <= new_column < n and min_value[new_row][new_column] == float("inf"):
                    min_value[new_row][new_column] = max(
                        current[0], grid[new_row][new_column])
                    queue.put(
                        (min_value[new_row][new_column], new_row, new_column))
        result = [0] * k
        for i in range(k):
            current = queries[i]
            left = 0
            right = n * m
            while left < right:
                mid = left + (right - left + 1) // 2
                if threshold[mid] < current:
                    left = mid
                else:
                    right = mid - 1
            result[i] = left
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
