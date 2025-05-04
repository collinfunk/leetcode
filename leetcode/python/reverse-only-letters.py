#!/usr/bin/env python3

""" Leetcode problem 917: Reverse Only Letters. """


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        result = []
        j = len(s) - 1
        for i, c in enumerate(s):
            if c.isalpha():
                while not s[j].isalpha():
                    j -= 1
                result.append(s[j])
                j -= 1
            else:
                result.append(c)
        return ''.join(result)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
