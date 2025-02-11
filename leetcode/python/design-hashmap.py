#!/usr/bin/env python3

""" Leetcode problem 706: Design HashMap. """


class MyHashMap:

    def __init__(self):
        self.values = {}

    def put(self, key: int, value: int) -> None:
        self.values[key] = value

    def get(self, key: int) -> int:
        try:
            return self.values[key]
        except KeyError:
            return -1

    def remove(self, key: int) -> None:
        try:
            del self.values[key]
        except KeyError:
            pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
