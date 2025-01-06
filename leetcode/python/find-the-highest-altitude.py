#!/usr/bin/env python3

""" Leetcode problem 1732: Find the Highest Altitude. """

from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_altitude = 0
        current_altitude = 0

        for value in gain:
            current_altitude += value
            if current_altitude > highest_altitude:
                highest_altitude = current_altitude

        return highest_altitude


def main() -> None:
    pass


if __name__ == "__main__":
    main()
