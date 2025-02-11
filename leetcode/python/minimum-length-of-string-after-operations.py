#!/usr/bin/env python3

""" Leetcode problem 3223: Minimum Length of String After Operations. """

from collections import defaultdict


class Solution:
    def minimumLength(self, s: str) -> int:
        table = defaultdict(int)
        x = 0
        for character in s:
            table[character] += 1
        for count in table.values():
            if count % 2 == 1:
                x += count - 1
            else:
                x += count - 2
        return len(s) - x


def main() -> None:
    pass


if __name__ == "__main__":
    main()
