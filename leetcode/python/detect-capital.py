#!/usr/bin/env python3

""" Leetcode problem 520: Detect Capital. """


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word[0].isupper():
            if len(word) == 1:
                return True
            elif word[1].isupper():
                for character in word[2:]:
                    if not character.isupper():
                        return False
            else:
                for character in word[2:]:
                    if character.isupper():
                        return False
        else:
            for character in word[1:]:
                if character.isupper():
                    return False
        return True


def main() -> None:
    pass


if __name__ == "__main__":
    main()
