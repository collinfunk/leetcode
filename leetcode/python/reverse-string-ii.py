#!/usr/bin/env python3

""" Leetcode problem 541: Reverse String II. """


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = list(s)
        for i in range(0, len(result), 2 * k):
            result[i: i + k] = reversed(result[i: i + k])
        return ''.join(result)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
