#!/usr/bin/env python3

""" Leetcode problem 3174: Clear Digits. """

from collections import deque


class Solution:
    def clearDigits(self, s: str) -> str:
        stack = deque()

        for character in s:
            if character.isdigit():
                try:
                    stack.pop()
                except IndexError:
                    pass
            else:
                stack.append(character)
        return ''.join(stack)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
