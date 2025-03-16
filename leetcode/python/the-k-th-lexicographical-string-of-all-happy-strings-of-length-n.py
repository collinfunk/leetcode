#!/usr/bin/env python3

""" Leetcode problem 1415: The k-th Lexicographical String of All Happy Strings of Length n. """


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy_strings = []

        def visit(current: str) -> None:
            nonlocal n
            if len(current) == n:
                happy_strings.append(current)
                return
            for ch in ['a', 'b', 'c']:
                if len(current) > 0 and current[-1] == ch:
                    continue
                visit(current + ch)
        visit('')
        if len(happy_strings) < k:
            return ''
        return happy_strings[k - 1]


def main() -> None:
    pass


if __name__ == "__main__":
    main()
