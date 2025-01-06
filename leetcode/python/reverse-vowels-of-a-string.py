#!/usr/bin/env python3

""" Leetcode problem 345: Reverse Vowels of a String. """

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('AEIOUaeiou')
        str = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and str[left] not in vowels:
                left += 1
            while left < right and str[right] not in vowels:
                right -= 1
            temp = str[left]
            str[left] = str[right]
            str[right] = temp
            left += 1
            right -= 1
        return ''.join(str)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
