#!/usr/bin/env python3

""" Leetcode problem 617: Merge Two Binary Trees. """


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:
        if not root1 and not root2:
            return None
        result = TreeNode((root1.val if root1 else 0) +
                          (root2.val if root2 else 0))
        result.left = self.mergeTrees(
            root1 and root1.left, root2 and root2.left)
        result.right = self.mergeTrees(
            root1 and root1.right, root2 and root2.right)
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
