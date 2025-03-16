#!/usr/bin/env python3

""" Leetcode problem 1309: Decrypt String from Alphabet to Integer Mapping. """


class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = []
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                result.append(chr(int(s[i: i + 2]) + 96))
                i += 3
            else:
                result.append(chr(int(s[i]) + 96))
                i += 1
        return ''.join(result)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
