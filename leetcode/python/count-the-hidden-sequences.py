#!/usr/bin/env python3

""" Leetcode problem 2145: Count the Hidden Sequences. """


class Solution:
    def numberOfArrays(self, differences: list[int], lower: int, upper: int) -> int:
        x = 0
        y = 0
        current = 0
        for difference in differences:
            current += difference
            x = min(x, current)
            y = max(y, current)
            if y - x > upper - lower:
                return 0
        return (upper - lower) - (y - x) + 1


def main() -> None:
    pass


if __name__ == "__main__":
    main()
