#!/usr/bin/env python3

""" Leetcode problem 504: Base 7. """


class Solution:
    def convertToBase7(self, num: int) -> str:
        result = []
        if num == 0:
            return "0"
        elif num < 0:
            num = -num
            negative = True
        else:
            negative = False
        while num > 0:
            result.append(str(num % 7))
            num //= 7
        if negative:
            return "-" + "".join(result[::-1])
        else:
            return "".join(result[::-1])


def main() -> None:
    pass


if __name__ == "__main__":
    main()
