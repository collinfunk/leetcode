#!/usr/bin/env python3

""" Leetcode problem 19: Remove Nth Node From End of List. """


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head
        lead = dummy
        removed = dummy
        for _ in range(n + 1):
            lead = lead.next
        while lead:
            lead = lead.next
            removed = removed.next
        removed.next = removed.next.next
        return dummy.next


def main() -> None:
    pass


if __name__ == "__main__":
    main()
