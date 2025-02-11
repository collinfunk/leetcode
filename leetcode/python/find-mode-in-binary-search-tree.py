#!/usr/bin/env python3

""" Leetcode problem 501: Find Mode in Binary Search Tree. """

from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        table = defaultdict(int)
        maximum_count = 0
        result = []

        def visit(node: TreeNode | None) -> None:
            nonlocal table, maximum_count, result
            if not node:
                return
            visit(node.left)
            table[node.val] += 1
            if maximum_count < table[node.val]:
                maximum_count = table[node.val]
                result = [node.val]
            elif maximum_count == table[node.val]:
                result.append(node.val)
            visit(node.right)
        visit(root)
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
