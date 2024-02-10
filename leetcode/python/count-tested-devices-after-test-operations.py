#!/usr/bin/env python3

""" Leetcode problem 2960: Count Tested Devices After Test Operations. """

from typing import List


class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        n = len(batteryPercentages)
        result = 0
        for i in range(0, n):
            if batteryPercentages[i] - result > 0:
                result += 1
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
