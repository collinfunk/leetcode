#!/usr/bin/env python3

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.check_nodes(root, root)

    def check_nodes(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return self.check_nodes(left.left, right.right) and self.check_nodes(left.right, right.left)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
