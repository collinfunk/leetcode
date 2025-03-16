#!/usr/bin/env python3

""" Leetcode problem 2022: Convert 1D Array Into 2D Array. """


class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if m * n != len(original):
            return []
        result = []
        for i in range(0, len(original), n):
            result.append(original[i: i + n])
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
