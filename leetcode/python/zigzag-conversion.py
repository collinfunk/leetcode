#!/usr/bin/env python3

""" Leetcode problem 6: Zigzag Conversion. """


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [""] * numRows
        row_index = 0
        up = True
        for character in s:
            rows[row_index] += character
            if row_index + 1 == numRows:
                up = False
            elif row_index == 0:
                up = True
            if up:
                row_index += 1
            else:
                row_index -= 1
        return "".join(rows)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
