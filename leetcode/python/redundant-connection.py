#!/usr/bin/env python3

""" Leetcode problem 684: Redundant Connection. """


class UnionFind:
    def __init__(self, x: int) -> None:
        self.parent = [*range(x)]
        self.rank = [1] * x

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return True
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        return False


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        uf = UnionFind(len(edges) + 1)
        for u, v in edges:
            if uf.union(u, v):
                return [u, v]


def main() -> None:
    pass


if __name__ == "__main__":
    main()
