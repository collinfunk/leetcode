#!/usr/bin/env python3

""" Leetcode problem 1047: Remove All Adjacent Duplicates In String. """


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if 0 < len(stack) and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
