#!/usr/bin/env python3

""" Leetcode problem 1791: Find Center of Star Graph. """


class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        if edges[0][0] == edges[1][0]:
            return edges[0][0]
        if edges[0][0] == edges[1][1]:
            return edges[1][1]
        return edges[0][1]


def main() -> None:
    pass


if __name__ == "__main__":
    main()
