#!/usr/bin/env python3

""" Leetcode problem 3042: Count Prefix and Suffix Pairs I. """

from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        result = 0
        for i in range(0, len(words)):
            for j in range(i + 1, len(words)):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    result += 1
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
