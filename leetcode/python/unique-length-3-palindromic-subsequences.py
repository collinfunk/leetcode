#!/usr/bin/env python3

""" Leetcode problem 1930: Unique Length-3 Palindromic Subsequences. """


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left = [-1] * 26
        right = [-1] * 26
        result = 0
        for i in range(0, len(s)):
            current = ord(s[i]) - ord("a")
            if left[current] == -1:
                left[current] = i
            right[current] = i
        for i in range(0, 26):
            if left[i] != -1:
                middle = set()
                for j in range(left[i] + 1, right[i]):
                    middle.add(s[j])
                result += len(middle)
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
