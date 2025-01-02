#!/usr/bin/env python3

""" Leetcode problem 1768: Merge Strings Alternately. """


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        index1 = 0
        index2 = 0
        result = ""

        while index1 < len(word1) or index2 < len(word2):
            if (not index2 < len(word2)) or index1 <= index2 and index1 < len(word1):
                result += word1[index1]
                index1 += 1
            else:
                result += word2[index2]
                index2 += 1

        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
