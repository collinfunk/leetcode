#!/usr/bin/env python3

""" Leetcode problem 530: Minimum Absolute Difference in BST. """

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return
        if root.left:
            self.traverse(root.left)
        if root.val - self.prev < self.min_dist:
            self.min_dist = root.val - self.prev
        self.prev = root.val
        if root.right:
            self.traverse(root.right)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min_dist = float('inf')
        self.prev = float('-inf')
        self.traverse(root)
        return self.min_dist


def main() -> None:
    pass


if __name__ == "__main__":
    main()
