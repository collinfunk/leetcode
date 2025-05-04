#!/usr/bin/env python3

""" Leetcode problem 1534: Count Good Triplets. """


class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        result = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        result += 1
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
