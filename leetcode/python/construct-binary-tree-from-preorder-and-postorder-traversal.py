#!/usr/bin/env python3

""" Leetcode problem 889: Construct Binary Tree from Preorder and Postorder Traversal. """


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> TreeNode | None:
        def dfs() -> TreeNode | None:
            node = TreeNode(postorder.pop())
            if node.val != preorder[-1]:
                node.right = dfs()
            if node.val != preorder[-1]:
                node.left = dfs()
            preorder.pop()
            return node
        return dfs()


def main() -> None:
    pass


if __name__ == "__main__":
    main()
