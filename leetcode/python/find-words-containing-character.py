#!/usr/bin/env python3

""" Leetcode problem 2942: Find Words Containing Character. """

from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i in range(0, len(words)):
            if x in set(words[i]):
                result.append(i)
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
