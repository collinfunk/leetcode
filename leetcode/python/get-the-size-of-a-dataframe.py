#!/usr/bin/env python3

""" Leetcode problem 2878: Get the Size of a DataFrame. """

from typing import List
import pandas as pd


def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [players.shape[0], players.shape[1]]


def main() -> None:
    pass


if __name__ == "__main__":
    main()
