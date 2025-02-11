#!/usr/bin/env python3

""" Leetcode problem 2788: Split Strings by Separator. """


class Solution:
    def splitWordsBySeparator(self, words: list[str], separator: str) -> list[str]:
        return [w for word in words for w in word.split(separator) if w]


def main() -> None:
    pass


if __name__ == "__main__":
    main()
