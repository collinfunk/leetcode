#!/usr/bin/env python3

""" Leetcode problem 80: Remove Duplicates from Sorted Array II. """


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        previous = float('-inf')
        seen = 0
        index = 0
        for i in range(len(nums)):
            if nums[i] == previous:
                seen += 1
            else:
                seen = 0
            if seen < 2:
                nums[index] = nums[i]
                index += 1
            previous = nums[i]
        return index


def main() -> None:
    pass


if __name__ == "__main__":
    main()
