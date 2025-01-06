#!/usr/bin/env python3

""" Leetcode problem 1207: Unique Number of Occurrences. """

from typing import List
from collections import defaultdict


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        table = defaultdict(int)
        for value in arr:
            table[value] += 1
        counts = set()
        for value, occurrences in table.items():
            if occurrences in counts:
                return False
            counts.add(occurrences)
        return True


def main() -> None:
    pass


if __name__ == "__main__":
    main()
