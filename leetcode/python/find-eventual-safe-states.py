#!/usr/bin/env python3

""" Leetcode problem 802: Find Eventual Safe States. """

from typing import List
from collections import deque


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        result = []
        indegree = [0] * n
        adj = [[] for _ in range(n)]
        for i in range(n):
            for node in graph[i]:
                adj[node].append(i)
                indegree[i] += 1
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        safe = [False] * n
        while queue:
            node = queue.popleft()
            safe[node] = True
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        safe_nodes = []
        for i in range(n):
            if safe[i]:
                safe_nodes.append(i)
        return safe_nodes


def main() -> None:
    pass


if __name__ == "__main__":
    main()
