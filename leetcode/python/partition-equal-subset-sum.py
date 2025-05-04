#!/usr/bin/env python3

""" Leetcode problem 416: Partition Equal Subset Sum. """


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [True] + ([False] * target)
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        return dp[target]


def main() -> None:
    pass


if __name__ == "__main__":
    main()
