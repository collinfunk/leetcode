#!/usr/bin/env python3

""" Leetcode problem 1323: Maximum 69 Number. """


class Solution:
    def maximum69Number(self, num: int) -> int:
        digits = list(str(num))
        try:
            six = digits.index('6')
        except ValueError:
            return num
        digits[six] = '9'
        return int(''.join(digits))


def main() -> None:
    pass


if __name__ == "__main__":
    main()
