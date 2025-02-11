#!/usr/bin/env python3

""" Leetcode problem 1752. Check if Array Is Sorted and Rotated. """


class Solution:
    def check(self, nums: list[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True
        inversion = 0
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                inversion += 1
        if nums[0] < nums[n - 1]:
            inversion += 1
        return inversion <= 1


def main() -> None:
    pass


if __name__ == "__main__":
    main()
