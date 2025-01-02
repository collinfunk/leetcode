#!/usr/bin/env python3

""" Leetcode problem 222: Count Complete Tree Nodes. """

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

        self.traverse(root.left)
        self.traverse(root.right)

        self.count += 1

    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.traverse(root)
        return self.count


def main() -> None:
    pass


if __name__ == "__main__":
    main()
