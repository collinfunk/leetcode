#!/usr/bin/env python3

""" Leetcode problem 2116: Check if a Parentheses String Can Be Valid. """


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
        unlocked = 0
        opened = 0
        closed = 0
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '0':
                unlocked += 1
            elif s[i] == '(':
                opened += 1
            elif s[i] == ')':
                closed += 1
            if unlocked - opened + closed < 0:
                return False
        unlocked = 0
        opened = 0
        closed = 0
        for i in range(0, len(s)):
            if locked[i] == '0':
                unlocked += 1
            elif s[i] == '(':
                opened += 1
            elif s[i] == ')':
                closed += 1
            if unlocked + opened - closed < 0:
                return False
        return True


def main() -> None:
    pass


if __name__ == "__main__":
    main()
