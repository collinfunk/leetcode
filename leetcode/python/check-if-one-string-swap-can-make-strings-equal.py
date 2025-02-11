#!/usr/bin/env python3

""" Leetcode problem 1790: Check if One String Swap Can Make Strings Equal. """


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        different = []
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
                different.append(i)
        if count != 2:
            return False
        return s1[different[0]] == s2[different[1]] and s1[different[1]] == s2[different[0]]


def main() -> None:
    pass


if __name__ == "__main__":
    main()
