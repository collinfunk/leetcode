#!/usr/bin/env python3

""" Leetcode problem 171: Excel Sheet Column Number. """


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i in range(0, len(columnTitle)):
            result *= 26
            result += ord(columnTitle[i]) - ord('A') + 1
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
