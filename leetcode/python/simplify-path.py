#!/usr/bin/env python3

""" Leetcode problem 71: Simplify Path. """


class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = [part for part in path.split('/') if part]
        result = []
        for part in parts:
            if part == '.':
                continue
            if part == '..':
                try:
                    result.pop()
                except IndexError:
                    pass
                continue
            result.append(part)
        return '/' + '/'.join(result)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
