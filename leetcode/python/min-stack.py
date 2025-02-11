#!/usr/bin/env python3

""" Leetcode problem 155: Min Stack. """

from collections import deque


class MinStack:

    def __init__(self):
        self.stack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
