#!/usr/bin/env python3

""" Leetcode problem 2698: Find the Punishment Number of an Integer. """


class Solution:
    def punishmentNumber(self, n: int) -> int:
        values = [1, 9, 10, 36, 45, 55, 82, 91, 99, 100, 235, 297, 369,
                  370, 379, 414, 657, 675, 703, 756, 792, 909, 918,
                  945, 964, 990, 991, 999, 1000]
        result = 0
        for value in values:
            if value <= n:
                result += value * value
            else:
                break
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
