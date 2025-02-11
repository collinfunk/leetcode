#!/usr/bin/env python3

""" Leetcode problem 2889: Reshape Data: Pivot. """

import pandas as pd


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index='month', columns='city', values='temperature')


def main() -> None:
    pass


if __name__ == "__main__":
    main()
