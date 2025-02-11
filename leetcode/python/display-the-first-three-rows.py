#!/usr/bin/env python3

""" Leetcode problem 2879: Display the First Three Rows. """

import pandas as pd


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
