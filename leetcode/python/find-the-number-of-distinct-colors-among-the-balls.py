#!/usr/bin/env python3

""" Leetcode problem 3160. Find the Number of Distinct Colors Among the Balls. """

from collections import defaultdict


class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        table = {}
        frequency = defaultdict(int)
        result = []
        for ball, color in queries:
            if ball in table:
                old_color = table[ball]
                frequency[old_color] -= 1
                if frequency[old_color] == 0:
                    del frequency[old_color]
            table[ball] = color
            frequency[color] += 1
            result.append(len(frequency))
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
