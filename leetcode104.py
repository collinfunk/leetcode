#!/usr/bin/env python3

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root, 0)

    def traverse(self, root: Optional[TreeNode], depth: int) -> int:
        if not root:
            return depth
        else:
            return max(self.traverse(root.left, depth + 1), self.traverse(root.right, depth + 1))


def main() -> None:
    pass


if __name__ == "__main__":
    main()
