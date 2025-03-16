#!/usr/bin/env python3

""" Leetcode problem 2161: Partition Array According to Given Pivot. """


class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        result = [0] * len(nums)
        less = 0
        greater = len(nums) - 1
        for i, j in zip(range(len(nums)), range(len(nums) - 1, -1, -1)):
            if nums[i] < pivot:
                result[less] = nums[i]
                less += 1
            if nums[j] > pivot:
                result[greater] = nums[j]
                greater -= 1
        while less <= greater:
            result[less] = pivot
            less += 1
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
