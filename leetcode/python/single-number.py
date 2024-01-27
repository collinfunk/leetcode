#!/usr/bin/env python3

""" Leetcode problem 136: Single Number. """

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_table = set()
        possibility_list = list()

        for value in nums:
            if value in seen_table:
                possibility_list.remove(value)
            else:
                seen_table.add(value)
                possibility_list.append(value)

        return possibility_list[0]


def main() -> None:
    pass


if __name__ == "__main__":
    main()
