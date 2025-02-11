#!/usr/bin/env python3

"""Leetcode problem 2891: Method Chaining."""

import pandas as pd


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals.loc[animals['weight'] > 100].sort_values(
        by='weight', ascending=False
    )[['name']]


def main() -> None:
    pass


if __name__ == "__main__":
    main()
