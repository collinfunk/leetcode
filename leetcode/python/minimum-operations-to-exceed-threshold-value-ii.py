#!/usr/bin/env python3

""" Leetcode problem 3066: Minimum Operations to Exceed Threshold Value II. """

import heapq


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        queue = nums
        heapq.heapify(queue)
        result = 0
        while len(nums) > 1:
            x = heapq.heappop(queue)
            y = heapq.heappop(queue)
            if x >= k:
                return result
            value = min(x, y) * 2 + max(x, y)
            heapq.heappush(queue, value)
            result += 1
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
