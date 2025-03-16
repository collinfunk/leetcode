#!/usr/bin/env python3

""" Leetcode problem 476: Number Complement. """


class Solution:
    def findComplement(self, num: int) -> int:
        return num ^ ((1 << num.bit_length()) - 1)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
