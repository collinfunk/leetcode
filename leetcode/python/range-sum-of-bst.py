#!/usr/bin/env python3

""" Leetcode problem 938: Range Sum of BST. """


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        result = 0

        def visit(node: TreeNode | None) -> None:
            nonlocal low, high, result
            if not node:
                return
            if node.val >= low and node.val <= high:
                result += node.val
            visit(node.left)
            visit(node.right)
        visit(root)
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
