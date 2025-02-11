#!/usr/bin/env python3

""" Leetcode problem 404: Sum of Left Leaves. """


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        result = 0

        def visit(node: TreeNode | None, left_child: bool) -> None:
            nonlocal result
            if not node:
                return
            if left_child and node.right is None and node.left is None:
                result += node.val
            else:
                visit(node.left, True)
                visit(node.right, False)
        visit(root, False)
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
