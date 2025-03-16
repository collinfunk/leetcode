#!/usr/bin/env python3

""" Leetcode problem 1903: Largest Odd Number in String. """


class Solution:
    def largestOddNumber(self, num: str) -> str:
        return num.rstrip("02468")


def main() -> None:
    pass


if __name__ == "__main__":
    main()
