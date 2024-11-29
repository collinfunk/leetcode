#!/usr/bin/env python3

""" Leetcode problem 160: Intersection of Two Linked Lists. """

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None

        nodeA = headA
        nodeB = headB

        while nodeA != nodeB:
            if nodeA is None:
                nodeA = headB
            else:
                nodeA = nodeA.next
            if nodeB is None:
                nodeB = headA
            else:
                nodeB = nodeB.next

        return nodeA


def main() -> None:
    pass


if __name__ == "__main__":
    main()
