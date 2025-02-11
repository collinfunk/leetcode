#!/usr/bin/env python3

""" Leetcode problem 916: Word Subsets. """

from typing import List
from collections import defaultdict


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        table = {}
        for word in words2:
            counts = defaultdict(int)
            for letter in word:
                counts[letter] += 1
            for letter, count in counts.items():
                if letter in table:
                    table[letter] = max(count, table[letter])
                else:
                    table[letter] = count
        result = []
        for word in words1:
            include = True
            for key in table:
                if word.count(key) < table[key]:
                    include = False
                    break
            if include:
                result.append(word)
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
