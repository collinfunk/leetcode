#!/usr/bin/env python3

""" Leetcode problem 242: Valid Anagram. """


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        s_counts = dict()

        if s_len != t_len:
            return False

        for character in s:
            if s_counts.get(character) is None:
                s_counts[character] = 1
            else:
                s_counts[character] += 1

        for character in t:
            if s_counts.get(character) is None or s_counts.get(character) == 0:
                return False
            s_counts[character] -= 1

        return True


def main() -> None:
    pass


if __name__ == "__main__":
    main()
