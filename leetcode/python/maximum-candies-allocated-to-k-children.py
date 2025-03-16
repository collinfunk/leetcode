#!/usr/bin/env python3

""" Leetcode problem 2226: Maximum Candies Allocated to K Children. """


class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        max_pile = 0
        for candy in candies:
            max_pile = max(max_pile, candy)
        left = 0
        right = max_pile
        while left < right:
            middle = (left + right + 1) // 2
            flag = False
            max_per_child = 0
            for pile in candies:
                max_per_child += pile // middle
            if k <= max_per_child:
                left = middle
            else:
                right = middle - 1
        return left


def main() -> None:
    pass


if __name__ == "__main__":
    main()
