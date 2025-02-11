#!/usr/bin/env python3

""" Leetcode problem 637: Average of Levels in Binary Tree. """

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, root: Optional[TreeNode], level: int) -> None:
        if not root:
            return
        try:
            self.levels[level].append(root.val)
        except IndexError:
            self.levels.append([root.val])

        self.traverse(root.left, level + 1)
        self.traverse(root.right, level + 1)

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.levels = []
        self.traverse(root, 0)
        result = []
        for i in range(len(self.levels)):
            result.append(sum(self.levels[i]) / len(self.levels[i]))
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
