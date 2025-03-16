#!/usr/bin/env python3

""" Leetcode problem 2594: Minimum Time to Repair Cars. """

from collections import Counter
import heapq


class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        count = Counter(ranks)
        heap = [[rank, rank, 1, count[rank]] for rank in count]
        heapq.heapify(heap)
        while 0 < cars:
            time, rank, n, count = heapq.heappop(heap)
            cars -= count
            n += 1
            heapq.heappush(heap, [rank * n * n, rank, n, count])
        return time


def main() -> None:
    pass


if __name__ == "__main__":
    main()
