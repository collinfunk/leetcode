#!/usr/bin/env python3

""" Leetcode problem 83: Remove Duplicates from Sorted List. """

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        current_node = head
        while current_node:
            if not current_node.next:
                break
            elif current_node.val == current_node.next.val:
                current_node.next = current_node.next.next
                continue
            current_node = current_node.next

        return head


def main() -> None:
    pass


if __name__ == "__main__":
    main()
