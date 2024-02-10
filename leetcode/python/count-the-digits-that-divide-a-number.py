#!/usr/bin/env python3

""" Leetcode problem 2520: Count the Digits That Divide a Number. """


class Solution:
    def countDigits(self, num: int) -> int:
        result = 0
        for character in str(num):
            if num % int(character) == 0:
                result += 1
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
