#!/usr/bin/env python3

""" Leetcode problem 500: Keyboard Row. """


class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        result = []
        row_1 = set(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'])
        row_2 = set(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'])
        row_3 = set(['z', 'x', 'c', 'v', 'b', 'n', 'm'])
        for word in words:
            w = word.lower()
            bad = False
            if w[0] in row_1:
                for c in w[1:]:
                    if c not in row_1:
                        bad = True
                        break
            elif w[0] in row_2:
                for c in w[1:]:
                    if c not in row_2:
                        bad = True
                        break
            else:
                for c in w[1:]:
                    if c not in row_3:
                        bad = True
                        break
            if not bad:
                result.append(word)
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
