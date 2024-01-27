#!/usr/bin/env python3

""" Leetcode problem 141: Linked List Cycle. """

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        leader = head
        trailer = head
        while leader and leader.next:
            leader = leader.next.next
            trailer = trailer.next
            if leader == trailer:
                return True
        return False


def main() -> None:
    pass


if __name__ == "__main__":
    main()
