#!/usr/bin/env python3

""" Leetcode problem 1684: Count the Number of Consistent Strings. """

from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        table = set(allowed)
        result = 0
        for word in words:
            include = True
            for letter in word:
                if letter not in table:
                    include = False
                    break
            if include:
                result += 1
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
