#!/usr/bin/env python3

""" Leetcode problem 3403: Find the Lexicographically Largest String From the Box I. """


class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        split_length = n - numFriends
        max_char = max(word)
        return max(word[i: i + split_length + 1] for i in range(n) if word[i] == max_char)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
