#!/usr/bin/env python3

""" Leetcode problem 46: Permutations. """

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.dfs(nums, [], [False] * len(nums), result)
        return result

    def dfs(self, nums: List[int], path: List[int], used: List[bool],
            result: List[List[int]]) -> None:
        if len(path) == len(nums):
            result.append(path[:])
        else:
            for i in range(0, len(nums)):
                if not used[i]:
                    path.append(nums[i])
                    used[i] = True
                    self.dfs(nums, path, used, result)
                    path.pop()
                    used[i] = False


def main() -> None:
    pass


if __name__ == "__main__":
    main()
