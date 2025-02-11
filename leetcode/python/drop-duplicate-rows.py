#!/usr/bin/env python3

""" Leetcode problem 2882: Drop Duplicate Rows. """

import pandas as pd


def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_duplicates(subset=['email'], inplace=True)
    return customers


def main() -> None:
    pass


if __name__ == "__main__":
    main()
