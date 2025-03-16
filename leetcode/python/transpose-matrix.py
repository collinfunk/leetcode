#!/usr/bin/env python3

""" Leetcode problem 867: Transpose Matrix. """


class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        m = len(matrix)
        n = len(matrix[0])
        result = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                result[j][i] = matrix[i][j]
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
