#!/usr/bin/env python3

""" Leetcode problem 1358: Number of Substrings Containing All Three Characters. """


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_position = [-1] * 3
        total = 0
        for i in range(len(s)):
            last_position[ord(s[i]) - ord('a')] = i
            total += 1 + min(last_position)
        return total


def main() -> None:
    pass


if __name__ == "__main__":
    main()
