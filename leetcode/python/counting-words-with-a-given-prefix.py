#!/usr/bin/env python3

""" Leetcode problem 2185: Counting Words With a Given Prefix. """

from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return len([word for word in words if word.startswith(pref)])


def main() -> None:
    pass


if __name__ == "__main__":
    main()
