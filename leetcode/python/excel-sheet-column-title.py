#!/usr/bin/env python3

""" Leetcode problem 168: Excel Sheet Column Title. """


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        while 0 < columnNumber:
            columnNumber -= 1
            result += str(chr(ord('A') + (columnNumber % 26)))
            columnNumber //= 26
        return result[::-1]


def main() -> None:
    pass


if __name__ == "__main__":
    main()
