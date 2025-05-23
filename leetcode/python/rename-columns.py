#!/usr/bin/env python3

""" Leetcode problem 2885: Rename Columns. """

import pandas as pd


def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students.rename(columns={'id': 'student_id',
                             'first': 'first_name',
                             'last': 'last_name',
                             'age': 'age_in_years'},
                    inplace=True)
    return students


def main() -> None:
    pass


if __name__ == "__main__":
    main()
