#!/usr/bin/env python3

""" Leetcode problem 2887: Fill Missing Data. """

import pandas as pd


def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products.fillna({'quantity': 0}, inplace=True)
    return products


def main() -> None:
    pass


if __name__ == "__main__":
    main()
