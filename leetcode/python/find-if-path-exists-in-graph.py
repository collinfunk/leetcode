#!/usr/bin/env python3

""" Leetcode problem 1971: Find if Path Exists in Graph. """

from collections import defaultdict
import heapq


class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        distances = {node: float('inf') for node in range(n)}
        distances[source] = 0
        queue = [(0, source)]
        while queue:
            current_distance, current_node = heapq.heappop(queue)
            if current_node == destination:
                return True
            if current_distance > distances[current_node]:
                continue
            for neighbor in graph[current_node]:
                distance = current_distance + 1
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))
        return False


def main() -> None:
    pass


if __name__ == "__main__":
    main()
