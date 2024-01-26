#!/usr/bin/env python3


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = dict()

        for character in magazine:
            if not counts.get(character):
                counts[character] = 1
            else:
                counts[character] += 1

        for character in ransomNote:
            if not counts.get(character) or counts.get(character) == 0:
                return False
            else:
                counts[character] -= 1

        return True


def main() -> None:
    pass


if __name__ == "__main__":
    main()
