#!/usr/bin/env python3

""" Leetcode problem 596: Classes More Than 5 Students. """

import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    counts = courses.groupby('class')['student'].count().reset_index()
    return counts[counts['student'] >= 5][['class']]


def main() -> None:
    pass


if __name__ == "__main__":
    main()
