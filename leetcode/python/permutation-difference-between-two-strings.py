#!/usr/bin/env python3

""" Leetcode problem 3146: Permutation Difference between Two Strings. """


class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        table = dict()
        result = 0
        for i, ch in enumerate(s):
            table[ch] = i
        for i, ch in enumerate(t):
            result += abs(table[ch] - i)
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
