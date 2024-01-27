#!/usr/bin/env python3

""" Leetcode problem 1816: Truncate Sentence. """


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split()[:k])


def main() -> None:
    pass


if __name__ == "__main__":
    main()
