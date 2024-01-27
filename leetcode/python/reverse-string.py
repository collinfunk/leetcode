#!/usr/bin/env python3

""" Leetcode problem 344: Reverse String. """

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]


def main() -> None:
    pass


if __name__ == "__main__":
    main()
