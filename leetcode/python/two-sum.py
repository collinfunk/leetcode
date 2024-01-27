#!/usr/bin/env python3

""" Leetcode problem 1: Two Sum. """

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = dict()

        for i in range(0, len(nums)):
            need = target - nums[i]
            if need in table:
                return [i, table[need]]
            table[nums[i]] = i

        return []


def main() -> None:
    pass


if __name__ == "__main__":
    main()
