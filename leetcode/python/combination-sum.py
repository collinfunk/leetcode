#!/usr/bin/env python3

""" Leetcode problem 39: Combination Sum. """

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) \
            -> List[List[int]]:
        table = dict()
        table[0] = [[]]
        candidates.sort()
        for candidate in candidates:
            for i in range(candidate, target + 1):
                if i - candidate in table:
                    if i not in table:
                        table[i] = []
                    for combination in table[i - candidate]:
                        table[i].append(combination + [candidate])
        return table[target] if target in table else []


def main() -> None:
    pass


if __name__ == "__main__":
    main()
