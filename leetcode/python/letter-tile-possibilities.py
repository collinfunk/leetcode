#!/usr/bin/env python3

""" Leetcode problem 1079: Letter Tile Possibilities. """

from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        seen = set()

        def dfs(current: str, remaining: Counter) -> None:
            nonlocal seen
            seen.add(current)
            for value in remaining.keys():
                if 0 < remaining[value]:
                    remaining[value] -= 1
                    dfs(current + value, remaining)
                    remaining[value] += 1
        dfs("", Counter(tiles))
        return len(seen) - 1


def main() -> None:
    pass


if __name__ == "__main__":
    main()
