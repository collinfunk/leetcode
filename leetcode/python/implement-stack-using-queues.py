#!/usr/bin/env python3

""" Leetcode problem 225: Implement Stack using Queues. """

from collections import deque


class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop()

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0


def main() -> None:
    pass


if __name__ == "__main__":
    main()
