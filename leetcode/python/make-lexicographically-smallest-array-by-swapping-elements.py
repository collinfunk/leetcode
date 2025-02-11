#!/usr/bin/env python3

""" Leetcode problem 2948: Make Lexicographically Smallest Array by Swapping Elements. """

from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        table = sorted((num, i) for i, num in enumerate(nums))
        new_position = []
        current_position = []
        prev = float('-inf')
        for num, i in table:
            if prev + limit < num:
                new_position.extend(sorted(current_position))
                current_position = [i]
            else:
                current_position.append(i)
            prev = num
        new_position.extend(sorted(current_position))
        result = [0] * n
        for i, j in enumerate(new_position):
            result[j] = table[i][0]
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
