#!/usr/bin/env python3

""" Leetcode problem 183: Customers Who Never Order. """

import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) \
        -> pd.DataFrame:
    return customers[~customers['id'].isin(orders['customerId'])][['name']] \
        .rename(columns={'name': 'Customers'})


def main() -> None:
    pass


if __name__ == "__main__":
    main()
