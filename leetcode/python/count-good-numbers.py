#!/usr/bin/env python3

""" Leetcode problem 1922: Count Good Numbers. """


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        modulo = (10 ** 9) + 7

        def mul(x: int, y: int) -> int:
            result = 1
            value = x
            while y > 0:
                if y % 2 == 1:
                    result = result * value % modulo
                value = value * value % modulo
                y //= 2
            return result
        return mul(5, (n + 1) // 2) * mul(4, n // 2) % modulo


def main() -> None:
    pass


if __name__ == "__main__":
    main()
