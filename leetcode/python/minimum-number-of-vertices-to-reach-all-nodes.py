#!/usr/bin/env python3

""" Leetcode problem 1557: Minimum Number of Vertices to Reach All Nodes. """


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        vertices = set(i for i in range(0, n))
        reachable = set(y for [x, y] in edges)
        return [vertex for vertex in vertices if vertex not in reachable]


def main() -> None:
    pass


if __name__ == "__main__":
    main()
