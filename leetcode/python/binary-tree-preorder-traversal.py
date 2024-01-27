#!/usr/bin/env python3

""" Leetcode problem 144: Binary Tree Preorder Traversal. """

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result_list = []
        self.traverse(root, result_list)
        return result_list

    def traverse(self, root: Optional[TreeNode], result_list: List[int]) -> None:
        if not root:
            return result_list
        else:
            result_list.append(root.val)
            self.traverse(root.left, result_list)
            self.traverse(root.right, result_list)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
