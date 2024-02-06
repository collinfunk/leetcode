#!/usr/bin/env python3

""" Leetcode problem 389: Find the Difference. """

from collections import defaultdict


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        character_map = defaultdict(int)
        for character in s:
            character_map[character] += 1
        for character in t:
            character_map[character] -= 1
        for character in character_map.keys():
            if (character_map[character] != 0):
                return f"{character}"
        return ""


def main() -> None:
    pass


if __name__ == "__main__":
    main()
