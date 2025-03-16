#!/usr/bin/env python3

""" Leetcode problem 832: Flipping an Image. """


class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        result = []
        for row in image:
            row.reverse()
            result.append([x ^ 1 for x in row])
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
