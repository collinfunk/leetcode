#!/usr/bin/env python3

""" Leetcode problem 2179: Count Good Triplets in an Array. """


class FenwickTree:
    def __init__(self, size: int) -> None:
        self.tree = [0] * (size + 1)

    def update(self, index: int, value: int) -> None:
        index += 1
        while index <= len(self.tree) - 1:
            self.tree[index] += value
            index += index & -index

    def query(self, index: int) -> int:
        index += 1
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result


class Solution:
    def goodTriplets(self, nums1: list[int], nums2: list[int]) -> int:
        pos2 = [0] * len(nums1)
        table = [0] * len(nums1)
        for i, num2 in enumerate(nums2):
            pos2[num2] = i
        for i, num1 in enumerate(nums1):
            table[pos2[num1]] = i
        tree = FenwickTree(len(nums1))
        result = 0
        for i in range(len(nums1)):
            pos = table[i]
            left = tree.query(pos)
            tree.update(pos, 1)
            right = (len(nums1) - 1 - pos) - (i - left)
            result += left * right
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
