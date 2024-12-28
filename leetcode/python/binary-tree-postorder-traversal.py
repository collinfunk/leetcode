#!/usr/bin/env python3

""" Leetcode problem 145: Binary Tree Postorder Traversal. """

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        result.extend(self.traverse(root.left))
        result.extend(self.traverse(root.right))
        result.append(root.val)
        return result

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.traverse(root)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
