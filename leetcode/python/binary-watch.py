#!/usr/bin/env python3

""" Leetcode problem 401: Binary Watch. """


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        result = []
        for hour in range(12):
            for minute in range(60):
                hour_ones = bin(hour).count('1')
                minute_ones = bin(minute).count('1')
                if hour_ones + minute_ones == turnedOn:
                    result.append(f'{hour}:{minute:02d}')
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
