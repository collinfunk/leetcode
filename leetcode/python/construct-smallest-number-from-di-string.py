#!/usr/bin/env python3

""" Leetcode problem 2375: Construct Smallest Number From DI String. """

from collections import deque


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        result = deque()
        number_stack = deque()
        for i in range(n + 1):
            number_stack.append(i + 1)
            if i == n or pattern[i] == 'I':
                while number_stack:
                    result.append(str(number_stack.pop()))
        return ''.join(result)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
