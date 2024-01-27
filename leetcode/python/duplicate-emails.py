#!/usr/bin/env python3

""" Leetcode problem 182: Duplicate Emails. """

import pandas as pd


def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    return person[person.duplicated(['email'], keep=False)] \
        .drop('id', axis=1).drop_duplicates()


def main() -> None:
    pass


if __name__ == "__main__":
    main()
