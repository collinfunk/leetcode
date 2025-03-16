#!/usr/bin/env python3

""" Leetcode problem 1028: Recover a Tree From Preorder Traversal. """


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode | None:
        levels = []
        n = len(traversal)
        index = 0
        while index < n:
            depth = 0
            while index < n and traversal[index] == '-':
                depth += 1
                index += 1
            value = 0
            while index < n and traversal[index].isdigit():
                value = value * 10 + int(traversal[index])
                index += 1
            node = TreeNode(value)
            if depth < len(levels):
                levels[depth] = node
            else:
                levels.append(node)
            if 0 < depth:
                parent = levels[depth - 1]
                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node
        return levels[0]


def main() -> None:
    pass


if __name__ == "__main__":
    main()
