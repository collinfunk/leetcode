#!/usr/bin/env python3

""" Leetcode problem 3108: Minimum Cost Walk in Weighted Graph. """


class Solution:
    def minimumCost(self, n: int, edges: list[list[int]], query: list[list[int]]) -> list[int]:
        parent = list(range(n))
        min_cost = [-1] * n

        def find_root(x: int) -> int:
            if parent[x] != x:
                parent[x] = find_root(parent[x])
            return parent[x]
        for start, end, weight in edges:
            start_root = find_root(start)
            end_root = find_root(end)
            min_cost[end_root] &= weight
            if start_root != end_root:
                min_cost[end_root] &= min_cost[start_root]
                parent[start_root] = end_root
        result = []
        for start, end in query:
            if start == end:
                result.append(0)
            elif find_root(start) != find_root(end):
                result.append(-1)
            else:
                result.append(min_cost[find_root(start)])
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
