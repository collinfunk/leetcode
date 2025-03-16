#!/usr/bin/env python3

""" Leetcode problem 965: Univalued Binary Tree. """


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: TreeNode | None) -> bool:
        flag = True

        def visit(node: TreeNode | None) -> None:
            nonlocal root, flag
            if not node or not flag:
                return
            if node.val != root.val:
                flag = False
            visit(node.right)
            visit(node.left)
        visit(root)
        return flag


def main() -> None:
    pass


if __name__ == "__main__":
    main()
