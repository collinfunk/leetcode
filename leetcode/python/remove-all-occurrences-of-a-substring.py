#!/usr/bin/env python3

""" Leetcode problem 1910: Remove All Occurrences of a Substring. """


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, '', 1)
        return s


def main() -> None:
    pass


if __name__ == "__main__":
    main()
