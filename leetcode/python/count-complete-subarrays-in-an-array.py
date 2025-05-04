#!/usr/bin/env python3

""" Leetcode problem 2799: Count Complete Subarrays in an Array. """


class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        distinct = len(set(nums))
        n = len(nums)
        table = {}
        result = 0
        right = 0
        for left in range(n):
            if left > 0:
                remove = nums[left - 1]
                table[remove] -= 1
                if table[remove] == 0:
                    table.pop(remove)
            while right < n and len(table) < distinct:
                add = nums[right]
                table[add] = table.get(add, 0) + 1
                right += 1
            if len(table) == distinct:
                result += n - right + 1
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
