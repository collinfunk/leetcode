#!/usr/bin/env python3

""" Leetcode problem 2661: First Completely Painted Row or Column. """

from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        table = {}
        for i in range(0, m):
            for j in range(0, n):
                table[mat[i][j]] = (i, j)
        row = [0] * m
        column = [0] * n
        for i in range(0, len(arr)):
            x, y = table[arr[i]]
            row[x] += 1
            column[y] += 1
            if row[x] == n or column[y] == m:
                return i
        return -1


def main() -> None:
    pass


if __name__ == "__main__":
    main()
