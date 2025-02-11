#!/usr/bin/env python3

""" Leetcode problem 409: Longest Palindrome. """

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = sum([(x // 2) * 2 for x in Counter(s).values()])
        if count == len(s):
            return count
        else:
            return count + 1


def main() -> None:
    pass


if __name__ == "__main__":
    main()
