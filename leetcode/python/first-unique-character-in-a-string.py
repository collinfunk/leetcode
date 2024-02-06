#!/usr/bin/env python3

""" Leetcode problem 49: First Unique Character in a String. """

from typing import List


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_map = dict()
        for character in s:
            count_map[character] = count_map.get(character, 0) + 1
        for i in range(0, len(s)):
            if count_map[s[i]] == 1:
                return i
        return -1


def main() -> None:
    pass


if __name__ == "__main__":
    main()
