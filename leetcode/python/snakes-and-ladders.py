#!/usr/bin/env python3

""" Leetcode problem 909: Snakes and Ladders. """

from collections import deque


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)

        def label_to_position(label: int) -> tuple[int, int]:
            r, c = divmod(label - 1, n)
            if r % 2 == 0:
                return n - 1 - r, c
            else:
                return n - 1 - r, n - 1 - c
        visited = set()
        queue = deque()
        queue.append((1, 0))
        while queue:
            label, next = queue.popleft()
            r, c = label_to_position(label)
            if board[r][c] != -1:
                label = board[r][c]
            if label == n * n:
                return next
            for x in range(1, 7):
                new_label = label + x
                if new_label <= n * n and new_label not in visited:
                    visited.add(new_label)
                    queue.append((new_label, next + 1))
        return -1


def main() -> None:
    pass


if __name__ == "__main__":
    main()
