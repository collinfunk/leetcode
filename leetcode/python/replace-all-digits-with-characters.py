#!/usr/bin/env python3

""" Leetcode problem 1844: Replace All Digits with Characters. """


class Solution:
    def replaceDigits(self, s: str) -> str:
        result = ""
        for i in range(0, len(s)):
            if i % 2 == 0:
                result += s[i]
            else:
                result += chr(ord(s[i - 1]) + int(s[i]))
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
