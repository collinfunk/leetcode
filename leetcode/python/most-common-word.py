#!/usr/bin/env python3

""" Leetcode problem 819: Most Common Word. """

from collections import defaultdict
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        table = defaultdict(int)
        banned_set = set(banned)
        regexp = re.compile(r'\W+')
        words = re.split(regexp, paragraph.lower())
        for word in words:
            if word and word not in banned_set:
                table[word] += 1
        return max(table, key=table.get)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
