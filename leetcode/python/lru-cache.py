#!/usr/bin/env python3

""" Leetcode problem 146: LRU Cache. """


class LRUCache:
    # Amount of elements we can have in the cache.
    capacity: int

    # Key value pair stored in the cache.
    mapping: dict[int, int]

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.mapping = dict()

    def get(self, key: int) -> int:
        result = self.mapping.get(key, -1)
        if result != -1:
            self.mapping[key] = self.mapping.pop(key)
        return result

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            self.mapping.pop(key)
        self.mapping[key] = value
        if len(self.mapping) > self.capacity:
            self.mapping.pop(next(iter(self.mapping)))


def main() -> None:
    pass


if __name__ == "__main__":
    main()
