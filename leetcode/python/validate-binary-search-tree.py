#!/usr/bin/env python3

""" Leetcode problem 98: Validate Binary Search Tree. """


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def validate(node: TreeNode | None, minimum: int | float, maximum: int | float) -> bool:
            if not node:
                return True
            if node.val <= minimum or maximum <= node.val:
                return False
            return validate(node.left, minimum, node.val) and validate(node.right, node.val, maximum)
        return validate(root, float('-inf'), float('inf'))


def main() -> None:
    pass


if __name__ == "__main__":
    main()
