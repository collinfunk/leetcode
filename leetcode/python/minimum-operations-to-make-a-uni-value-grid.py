#!/usr/bin/env python3

""" Leetcode problem 2033: Minimum Operations to Make a Uni-Value Grid. """


class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        values = sorted([value for row in grid for value in row])
        differences = [abs(value - values[0]) % x for value in values]
        if any(difference != 0 for difference in differences):
            return -1
        return sum(abs(value - values[len(values) // 2]) // x for value in values)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
