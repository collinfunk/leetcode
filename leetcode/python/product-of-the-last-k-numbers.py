#!/usr/bin/env python3

""" Leetcode problem 1352: Product of the Last K Numbers. """


class ProductOfNumbers:

    def __init__(self):
        self.products = [1]
        self.size = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.products = [1]
            self.size = 0
        else:
            self.products.append(self.products[self.size] * num)
            self.size += 1

    def getProduct(self, k: int) -> int:
        if self.size < k:
            return 0
        return self.products[self.size] // self.products[self.size - k]


def main() -> None:
    pass


if __name__ == "__main__":
    main()
