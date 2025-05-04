#!/usr/bin/env python3

""" Leetcode problem 1094: Car Pooling. """


class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        path = [0] * 1000
        for num, a, b in trips:
            for loc in range(a, b):
                path[loc] += num
                if path[loc] > capacity:
                    return False
        return True


def main() -> None:
    pass


if __name__ == "__main__":
    main()
