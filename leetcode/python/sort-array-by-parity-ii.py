#!/usr/bin/env python3

""" Leetcode problem 922: Sort Array By Parity II. """


class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        odd = []
        even = []
        result = []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        for i in range(len(even)):
            result.append(even[i])
            result.append(odd[i])
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
