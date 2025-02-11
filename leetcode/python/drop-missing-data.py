#!/usr/bin/env python3

""" Leetcode problem 2883: Drop Missing Data. """

import pandas as pd


def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students.dropna(subset=['name'], inplace=True)
    return students


def main() -> None:
    pass


if __name__ == "__main__":
    main()
