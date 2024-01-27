#!/usr/bin/env python3

""" Leetcode problem 66: Plus One. """

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits


def main() -> None:
    pass


if __name__ == "__main__":
    main()
