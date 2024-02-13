#!/usr/bin/env python3

""" Leetcode problem 111: Minimum Depth of Binary Tree. """

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root)

    def traverse(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = self.traverse(root.left)
        right_depth = self.traverse(root.right)
        if not root.left and not root.right:
            return 1
        if not root.left:
            return right_depth + 1
        if not root.right:
            return left_depth + 1
        return min(left_depth, right_depth) + 1


def main() -> None:
    pass


if __name__ == "__main__":
    main()
