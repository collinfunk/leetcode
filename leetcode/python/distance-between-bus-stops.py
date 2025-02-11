#!/usr/bin/env python3

""" Leetcode problem 1184: Distance Between Bus Stops. """


class Solution:
    def distanceBetweenBusStops(self, distance: list[int], start: int, destination: int) -> int:
        a = min(start, destination)
        b = max(start, destination)
        return min(sum(distance[a:b]), sum(distance) - sum(distance[a:b]))


def main() -> None:
    pass


if __name__ == "__main__":
    main()
