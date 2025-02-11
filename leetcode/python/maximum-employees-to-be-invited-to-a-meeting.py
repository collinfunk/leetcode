#!/usr/bin/env python3

""" Leetcode problem 2127: Maximum Employees to Be Invited to a Meeting. """

from collections import deque


class Solution:
    def maximumInvitations(self, favorite: list[int]) -> int:
        n = len(favorite)
        levels = [1] * n
        indegree = [0] * n
        for i in range(n):
            indegree[favorite[i]] += 1
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            node = queue.popleft()
            neighbor = favorite[node]
            indegree[neighbor] -= 1
            levels[neighbor] = levels[node] + 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
        longest_path = 0
        max_perimeter = 0
        for i in range(n):
            if indegree[i] != 0:
                node = i
                indegree[i] -= 1
                start = i
                perimeter = 1
                while favorite[node] != start:
                    node = favorite[node]
                    indegree[node] -= 1
                    perimeter += 1
                if perimeter == 2:
                    longest_path += levels[start] + levels[node]
                else:
                    max_perimeter = max(max_perimeter, perimeter)
        return max(max_perimeter, longest_path)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
