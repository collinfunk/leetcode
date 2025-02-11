#!/usr/bin/env python3

""" Leetcode problem 1221: Split a String in Balanced Strings. """


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        R_seen = 0
        L_seen = 0
        count = 0
        for ch in s:
            if ch == 'R':
                R_seen += 1
            else:  # ch == 'L'
                L_seen += 1
            if R_seen == L_seen:
                count += 1
        return count


def main() -> None:
    pass


if __name__ == "__main__":
    main()
