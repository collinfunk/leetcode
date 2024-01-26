#!/usr/bin/env python3

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for price in prices[1:]:
            if buy < price:
                profit = max(profit, price - buy)
            else:
                buy = price
        return profit


def main() -> None:
    pass


if __name__ == "__main__":
    main()
