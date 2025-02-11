#!/usr/bin/env python3

""" Leetcode problem 1185: Day of the Week. """

import datetime


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        value = datetime.datetime(year, month, day)
        return value.strftime('%A')


def main() -> None:
    pass


if __name__ == "__main__":
    main()
