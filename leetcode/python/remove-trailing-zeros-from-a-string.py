#!/usr/bin/env python3

""" Leetcode problem 2710: Remove Trailing Zeros From a String. """


class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip('0')


def main() -> None:
    pass


if __name__ == "__main__":
    main()
