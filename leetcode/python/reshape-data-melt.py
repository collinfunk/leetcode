#!/usr/bin/env python3

""" Leetcode problem 2890: Reshape Data: Melt. """

import pandas as pd


def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(report, id_vars=['product'],
                   value_vars=['quarter_1', 'quarter_2',
                               'quarter_3', 'quarter_4'],
                   var_name='quarter', value_name='sales')


def main() -> None:
    pass


if __name__ == "__main__":
    main()
