#!/usr/bin/env python3

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
