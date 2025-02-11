#!/usr/bin/env python3

""" Leetcode problem 2349: Design a Number Container System. """

from collections import defaultdict
import heapq


class NumberContainers:

    def __init__(self):
        self.queue = {}
        self.indexes = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.queue[index] = number
        heapq.heappush(self.indexes[number], index)

    def find(self, number: int) -> int:
        if number not in self.indexes:
            return -1
        while self.indexes[number]:
            i = self.indexes[number][0]
            if self.queue[i] == number:
                return i
            heapq.heappop(self.indexes[number])
        return -1


def main() -> None:
    pass


if __name__ == "__main__":
    main()
