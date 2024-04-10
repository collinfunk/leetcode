#!/usr/bin/env python3

""" Leetcode problem 23: Merge k Sorted Lists """

from collections import defaultdict

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        table = defaultdict(int)
        for current_list in lists:
            head = ListNode(0, current_list)
            head = head.next
            while head:
                table[head.val] += 1
                head = head.next
        head = ListNode(0)
        current = head
        order = sorted(table.keys(), reverse=True)
        while order:
            key = order.pop()
            for _ in range(table[key]):
                current.next = ListNode(key)
                current = current.next
        return head.next


def main() -> None:
    pass


if __name__ == "__main__":
    main()
