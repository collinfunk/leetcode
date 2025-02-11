#!/usr/bin/env python3

""" Leetcode problem 705: Design HashSet. """


class MyHashSet:

    def __init__(self):
        self.values = set()

    def add(self, key: int) -> None:
        self.values.add(key)

    def remove(self, key: int) -> None:
        self.values.discard(key)

    def contains(self, key: int) -> bool:
        return key in self.values


def main() -> None:
    pass


if __name__ == "__main__":
    main()
