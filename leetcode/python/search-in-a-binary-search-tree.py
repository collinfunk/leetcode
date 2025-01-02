#!/usr/bin/env python3

""" Leetcode problem 700: Search in a Binary Search Tree. """

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        while node:
            if node.val == val:
                return node
            elif node.val < val:
                node = node.right
            else:
                node = node.left
        return node


def main() -> None:
    pass


if __name__ == "__main__":
    main()
