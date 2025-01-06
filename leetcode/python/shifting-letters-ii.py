#!/usr/bin/env python3

""" Leetcode problem 2381: Shifting Letters II. """

from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        line = [0] * 50001
        value = 0
        for shift in shifts:
            line[shift[0]] += 1 if shift[2] else -1
            line[shift[1] + 1] += 1 if shift[2] else -1
        for i in range(0, len(s)):
            value = (value + line[i]) % 26
            s[i] = 'a' + (26 + (s[i] - 'a') + value) % 26
        return s


def main() -> None:
    pass


if __name__ == "__main__":
    main()
