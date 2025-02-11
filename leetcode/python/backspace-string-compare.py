#!/usr/bin/env python3

""" Leetcode problem 844. Backspace String Compare. """


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for character in s:
            if character == '#':
                try:
                    stack1.pop()
                except IndexError:
                    pass
            else:
                stack1.append(character)
        for character in t:
            if character == '#':
                try:
                    stack2.pop()
                except IndexError:
                    pass
            else:
                stack2.append(character)
        return stack1 == stack2


def main() -> None:
    pass


if __name__ == "__main__":
    main()
