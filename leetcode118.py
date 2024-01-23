#!/usr/bin/env python3

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(1, numRows):
            prev_row = result[i - 1]
            current_row = [1]
            for j in range(1, i):
                current_row.append(prev_row[j - 1] + prev_row[j])
            current_row.append(1)
            result.append(current_row)
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
