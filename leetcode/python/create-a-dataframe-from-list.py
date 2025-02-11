#!/usr/bin/env python3

""" Leetcode problem 2877: Create a DataFrame from List. """

from typing import List
import pandas as pd


def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=['student_id', 'age'])


def main() -> None:
    pass


if __name__ == "__main__":
    main()
