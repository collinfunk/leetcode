#!/usr/bin/env python3

""" Leetcode problem 48: Rotate Image. """

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] = zip(*matrix[::-1])


def main() -> None:
    pass


if __name__ == "__main__":
    main()
