#!/usr/bin/env python3

""" Leetcode problem 368: Largest Divisible Subset. """


class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [1] * len(nums)
        max_size = 1
        max_index = 0
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] > max_size:
                        max_size = dp[i]
                        max_index = i
        result = []
        num = nums[max_index]
        for i in range(max_index, -1, -1):
            if num % nums[i] == 0 and dp[i] == max_size:
                result.append(nums[i])
                num = nums[i]
                max_size -= 1
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
