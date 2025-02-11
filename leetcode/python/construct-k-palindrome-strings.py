#!/usr/bin/env python3

""" Leetcode problem 1400: Construct K Palindrome Strings. """


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        if len(s) == k:
            return True
        count = 0
        for c in s:
            count ^= 1 << (ord(c) - ord("a"))
        return bin(count).count("1") <= k


def main() -> None:
    pass


if __name__ == "__main__":
    main()
