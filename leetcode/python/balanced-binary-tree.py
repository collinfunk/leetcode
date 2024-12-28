#!/usr/bin/env python3

""" Leetcode problem 110: Balanced Binary Tree. """

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def height(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = self.height(root.left)
        if left < 0:
            return -1

        right = self.height(root.right)
        if right < 0:
            return -1

        if abs(left - right) > 1:
            return -1

        return max(left, right) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return 0 <= self.height(root)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
