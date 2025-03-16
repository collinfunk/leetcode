#!/usr/bin/env python3

""" Leetcode problem 2315. Count Asterisks. """


class Solution:
    def countAsterisks(self, s: str) -> int:
        return sum([x.count('*') for x in s.split('|')[::2]])


def main() -> None:
    pass


if __name__ == "__main__":
    main()
