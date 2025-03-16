#!/usr/bin/env python3

""" Leetcode problem 2342: Max Sum of a Pair With Equal Sum of Digits. """

from collections import defaultdict
import heapq


class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        table = defaultdict(list)
        for num in nums:
            value = num
            digit_sum = 0
            while value != 0:
                digit_sum += value % 10
                value //= 10
            table[digit_sum].append(num)
        result = -1
        for value in table.values():
            if len(value) > 1:
                top_two = heapq.nlargest(2, value)
                result = max(result, top_two[0] + top_two[1])
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
