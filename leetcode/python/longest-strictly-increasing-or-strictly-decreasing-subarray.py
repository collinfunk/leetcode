#!/usr/bin/env python3

""" Leetcode problem 3105: Longest Strictly Increasing or Strictly Decreasing Subarray. """


class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        increasing_length = 1
        decreasing_length = 1
        max_length = 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                increasing_length += 1
                decreasing_length = 1
            elif nums[i + 1] < nums[i]:
                decreasing_length += 1
                increasing_length = 1
            else:
                increasing_length = 1
                decreasing_length = 1
            max_length = max(max_length, increasing_length, decreasing_length)
        return max_length


def main() -> None:
    pass


if __name__ == "__main__":
    main()
