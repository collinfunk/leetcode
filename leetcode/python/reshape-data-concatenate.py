#!/usr/bin/env python3

""" Leetcode problem 2888: Reshape Data: Concatenate. """

import pandas as pd


def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2])


def main() -> None:
    pass


if __name__ == "__main__":
    main()
