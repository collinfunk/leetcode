#!/usr/bin/env python3

""" Leetcode problem 2886: Change Data Type. """

import pandas as pd


def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    return students.astype({'grade': int})


def main() -> None:
    pass


if __name__ == "__main__":
    main()
