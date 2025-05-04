#!/usr/bin/env python3

""" Leetcode problem 1399: Count Largest Group. """


from collections import Counter


class Solution:
    def countLargestGroup(self, n: int) -> int:
        table = Counter()
        for i in range(1, n + 1):
            table[sum([int(x) for x in str(i)])] += 1
        value = max(table.values())
        return sum(1 for x in table.values() if x == value)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
