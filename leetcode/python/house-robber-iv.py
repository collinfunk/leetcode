#!/usr/bin/env python3

""" Leetcode problem 2560: House Robber IV. """


class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:
        min_money = 1
        max_money = max(nums)
        while min_money < max_money:
            mid_money = (min_money + max_money) // 2
            possible = 0
            i = 0
            while i < len(nums):
                if nums[i] <= mid_money:
                    possible += 1
                    i += 2
                else:
                    i += 1
            if k <= possible:
                max_money = mid_money
            else:
                min_money = mid_money + 1
        return min_money


def main() -> None:
    pass


if __name__ == "__main__":
    main()
