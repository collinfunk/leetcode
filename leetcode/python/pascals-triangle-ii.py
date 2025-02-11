#!/usr/bin/env python3

""" Leetcode problem 119: Pascal's Triangle II. """

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1]]
        for i in range(1, rowIndex + 1):
            prev_row = triangle[i - 1]
            current_row = [1]
            for j in range(1, i):
                current_row.append(prev_row[j - 1] + prev_row[j])
            current_row.append(1)
            triangle.append(current_row)
        return triangle[rowIndex]


def main() -> None:
    pass


if __name__ == "__main__":
    main()
