#!/usr/bin/env python3

""" Leetcode problem 495: Teemo Attacking. """


class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        result = 0
        for i in range(len(timeSeries)):
            if i + 1 < len(timeSeries) and timeSeries[i] + duration > timeSeries[i + 1]:
                result += timeSeries[i + 1] - timeSeries[i]
            else:
                result += duration
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
