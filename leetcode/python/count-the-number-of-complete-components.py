#!/usr/bin/env python3

""" Leetcode problem 2685: Count the Number of Complete Components. """

from collections import defaultdict


class UnionFind:
    def __init__(self, x: int) -> None:
        self.parent = [-1] * x
        self.rank = [1] * x

    def find(self, x: int) -> int:
        if self.parent[x] == -1:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
            self.rank[x] += self.rank[y]
        else:
            self.parent[x] = y
            self.rank[y] += self.rank[x]


class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        uf = UnionFind(n)
        edge_count = defaultdict(int)
        for edge in edges:
            uf.union(edge[0], edge[1])
        for edge in edges:
            root = uf.find(edge[0])
            edge_count[root] += 1
        result = 0
        for vertex in range(n):
            if uf.find(vertex) == vertex:
                node_count = uf.rank[vertex]
                expected_edges = (node_count * (node_count - 1)) // 2
                if edge_count[vertex] == expected_edges:
                    result += 1
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
