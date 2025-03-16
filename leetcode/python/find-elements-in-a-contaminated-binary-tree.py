#!/usr/bin/env python3

""" Leetcode problem 1261: Find Elements in a Contaminated Binary Tree. """


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:

    def __init__(self, root: TreeNode | None) -> None:
        self.table = set()

        def visit(node: TreeNode | None, x: int) -> None:
            if not node:
                return
            node.val = x
            self.table.add(x)
            if node.left:
                visit(node.left, 2 * x + 1)
            if node.right:
                visit(node.right, 2 * x + 2)

        visit(root, 0)
        self.root = root

    def find(self, target: int) -> bool:
        return target in self.table


def main() -> None:
    pass


if __name__ == "__main__":
    main()
