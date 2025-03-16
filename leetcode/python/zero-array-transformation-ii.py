#!/usr/bin/env python3

""" Leetcode proble 3356: Zero Array Transformation II. """


class Solution:
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        total = 0
        result = 0
        difference = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            while total + difference[i] < nums[i]:
                result += 1
                if result > len(queries):
                    return -1
                left, right, value = queries[result - 1]
                if i <= right:
                    difference[max(left, i)] += value
                    difference[right + 1] -= value
            total += difference[i]
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
