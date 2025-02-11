#!/usr/bin/env python3

""" Leetcode problem 2884: Modify Columns. """

import pandas as pd


def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["salary"] *= 2
    return employees


def main() -> None:
    pass


if __name__ == "__main__":
    main()
