#!/usr/bin/env python3

""" Leetcode problem 49: Group Anagrams. """

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = dict()
        result = []
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in anagram_map:
                result[anagram_map[sorted_string]].append(string)
            else:
                anagram_map[sorted_string] = len(result)
                result.append([string])
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
