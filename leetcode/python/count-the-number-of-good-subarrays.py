#!/usr/bin/env python3

""" Leetcode problem 2537: Count the Number of Good Subarrays. """


from collections import Counter


class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        n = len(nums)
        result = 0
        same = 0
        right = -1
        count = Counter()
        for i in range(n):
            while same < k and right + 1 < n:
                right += 1
                same += count[nums[right]]
                count[nums[right]] += 1
            if same >= k:
                result += n - right
            count[nums[i]] -= 1
            same -= count[nums[i]]
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
