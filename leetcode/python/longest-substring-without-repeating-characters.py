#!/usr/bin/env python3

""" Leetcode problem 2: Longest Substring Without Repeating Characters. """


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        table = dict()
        result = 0
        start = 0
        for i in range(0, n):
            if s[i] in table:
                if table[s[i]] < start:
                    result = max(result, i - start + 1)
                else:
                    start = table[s[i]] + 1
            else:
                result = max(result, i - start + 1)
            table[s[i]] = i
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
