#!/usr/bin/env python3

""" Leetcode problem 1859: Sorting the Sentence. """


class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(' ')
        result = ["" for word in words]
        for word in words:
            index = ord(word[-1]) - ord('1')
            result[index] = word[:-1]
        return ' '.join(result)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
