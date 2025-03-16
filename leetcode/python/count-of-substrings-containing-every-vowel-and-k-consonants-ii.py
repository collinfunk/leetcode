#!/usr/bin/env python3

""" Leetcode problem 3306: Count of Substrings Containing Every Vowel and K Consonants II. """

from collections import defaultdict


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def at_least_k(word: str, k: int) -> int:
            vowels = set(['a', 'e', 'i', 'o', 'u'])
            result = 0
            start = 0
            end = 0
            vowel_count = defaultdict(int)
            consonant_count = 0
            while end < len(word):
                current = word[end]
                if current in vowels:
                    vowel_count[current] += 1
                else:
                    consonant_count += 1
                while len(vowel_count) == 5 and consonant_count >= k:
                    result += len(word) - end
                    start_letter = word[start]
                    if start_letter in vowels:
                        vowel_count[start_letter] -= 1
                        if vowel_count[start_letter] == 0:
                            vowel_count.pop(start_letter)
                    else:
                        consonant_count -= 1
                    start += 1
                end += 1
            return result
        return at_least_k(word, k) - at_least_k(word, k + 1)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
