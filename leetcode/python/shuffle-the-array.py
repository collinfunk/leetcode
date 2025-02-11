#!/usr/bin/env python3

""" Leetcode problem 1470: Shuffle the Array. """

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
