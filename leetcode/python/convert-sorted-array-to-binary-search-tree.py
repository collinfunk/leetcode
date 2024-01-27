#!/usr/bin/env python3

""" Leetcode problem 108: Convert Sorted Array to Binary Search Tree. """

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        nums_len = len(nums)
        if not nums_len:
            return None
        middle = nums_len // 2
        left = self.sortedArrayToBST(nums[:middle])
        right = self.sortedArrayToBST(nums[middle + 1:])
        return TreeNode(nums[middle], left, right)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
