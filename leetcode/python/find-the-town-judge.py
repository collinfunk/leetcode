#!/usr/bin/env python3

""" Leetcode problem 997: Find the Town Judge. """


class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        indegree = [0] * (n + 1)
        outdegree = [0] * (n + 1)
        for element in trust:
            indegree[element[1]] += 1
            outdegree[element[0]] += 1
        for i in range(1, n + 1):
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i
        return -1


def main() -> None:
    pass


if __name__ == "__main__":
    main()
