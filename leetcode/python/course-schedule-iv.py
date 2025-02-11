#!/usr/bin/env python3

""" Leetcode problem 1462: Course Schedule IV. """

from collections import defaultdict


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        table = defaultdict(list)
        for prerequisite in prerequisites:
            table[prerequisite[1]].append(prerequisite[0])
        result = []
        cache = {}

        def dfs(course: int, prerequisite: int) -> bool:
            if (course, prerequisite) in cache:
                return cache[(course, prerequisite)]
            for value in table[course]:
                if value == prerequisite or dfs(value, prerequisite):
                    cache[(course, prerequisite)] = True
                    return True
            cache[(course, prerequisite)] = False
            return False
        return [dfs(query[1], query[0]) for query in queries]


def main() -> None:
    pass


if __name__ == "__main__":
    main()
