#!/usr/bin/env python3

""" Leetcode problem 1071: Greatest Common Divisor of Strings. """


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        index1 = 0
        index2 = 0
        prefix_table = set()
        divisors = []

        while index1 < len(str1) and index2 < len(str2):
            if str1[index1] != str2[index2]:
                return ""
            prefix_table.add(str1[:index1 + 1])
            index1 += 1
            index2 += 1

        prefix_table.discard("")

        for prefix in prefix_table:
            if not (len(str1) / len(prefix)).is_integer():
                continue
            if not (len(str2) / len(prefix)).is_integer():
                continue
            if prefix * (len(str1) // len(prefix)) != str1:
                continue
            if prefix * (len(str2) // len(prefix)) != str2:
                continue
            divisors.append(prefix)

        longest_divisor = ""
        for divisor in divisors:
            if len(divisor) > len(longest_divisor):
                longest_divisor = divisor

        return longest_divisor


def main() -> None:
    pass


if __name__ == "__main__":
    main()
