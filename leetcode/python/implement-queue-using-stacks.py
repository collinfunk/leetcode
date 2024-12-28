#!/usr/bin/env python3

""" Leetcode problem 232: Implement Queue using Stacks. """

from collections import deque


class MyQueue:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.popleft()

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


def main() -> None:
    pass


if __name__ == "__main__":
    main()
