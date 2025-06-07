#!/usr/bin/env python3

""" Leetcode problem 3342: Find Minimum Time to Reach Last Room II. """

import heapq


class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = [(0, 0, 0, 1)]
        moveTime[0][0] = -1
        while queue:
            time, x, y, cost = heapq.heappop(queue)
            if x == n - 1 and y == m - 1:
                return time
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m and moveTime[nx][ny] != -1:
                    if time < moveTime[nx][ny]:
                        new_time = moveTime[nx][ny]
                    else:
                        new_time = time
                    new_time += cost
                    new_cost = 3 - cost
                    moveTime[nx][ny] = -1
                    heapq.heappush(queue, (new_time, nx, ny, new_cost))
            return -1


def main() -> None:
    pass


if __name__ == "__main__":
    main()
