#!/usr/bin/env python3

""" Leetcode problem 1123: Lowest Common Ancestor of Deepest Leaves. """


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode | None) -> TreeNode | None:
        def visit(node: TreeNode) -> tuple[int, TreeNode | None]:
            if not node:
                return (0, None)
            left = visit(node.left)
            right = visit(node.right)
            if right[0] < left[0]:
                return (left[0] + 1, left[1])
            if left[0] < right[0]:
                return (right[0] + 1, right[1])
            return (left[0] + 1, node)
        return visit(root)[1]


def main() -> None:
    pass


if __name__ == "__main__":
    main()
