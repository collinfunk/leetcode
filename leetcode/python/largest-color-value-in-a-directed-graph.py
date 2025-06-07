#!/usr/bin/env python3

""" Leetcode problem 1857: Largest Color Value in a Directed Graph. """

from collections import deque, defaultdict


class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        n = len(colors)
        graph = defaultdict(set)
        indegree = [0 for i in range(n)]
        for u, v in edges:
            graph[u].add(v)
            indegree[v] += 1
        queue = deque()
        option = [[0 for i in range(26)] for j in range(n)]
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        count = 0
        while queue:
            i = queue.popleft()
            option[i][ord(colors[i]) - ord('a')] += 1
            for j in graph[i]:
                for k in range(26):
                    option[j][k] = max(option[i][k], option[j][k])
                indegree[j] -= 1
                if indegree[j] == 0:
                    queue.append(j)
            count += 1
        if count != n:
            return -1
        return max([max(i) for i in option])


def main() -> None:
    pass


if __name__ == "__main__":
    main()
