#!/usr/bin/env python3

""" Leetcode problem 1976: Number of Ways to Arrive at Destination. """

import heapq


class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        graph = [[] for _ in range(n)]
        for start, end, time in roads:
            graph[start].append((end, time))
            graph[end].append((start, time))
        queue = [(0, 0)]
        shortest_time = [float("inf")] * n
        path_count = [0] * n
        shortest_time[0] = 0
        path_count[0] = 1
        while queue:
            current_time, current_node = heapq.heappop(queue)
            if current_time > shortest_time[current_node]:
                continue
            for neighbor_node, neighbor_time in graph[current_node]:
                if current_time + neighbor_time < shortest_time[neighbor_node]:
                    shortest_time[neighbor_node] = current_time + neighbor_time
                    path_count[neighbor_node] = path_count[current_node]
                    heapq.heappush(
                        queue, (shortest_time[neighbor_node], neighbor_node))
                elif current_time + neighbor_time == shortest_time[neighbor_node]:
                    path_count[neighbor_node] = (
                        path_count[neighbor_node] + path_count[current_node]) % ((10 ** 9) + 7)
        return path_count[n - 1]


def main() -> None:
    pass


if __name__ == "__main__":
    main()
