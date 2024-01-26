#!/usr/bin/env python3

class Solution:
    def isPalindrome(self, s: str) -> bool:
        low = 0
        high = len(s) - 1

        while low < high:
            if not str.isalnum(s[low]):
                low += 1
            elif not str.isalnum(s[high]):
                high -= 1
            elif s[low].lower() != s[high].lower():
                return False
            else:
                low += 1
                high -= 1
        return True


def main() -> None:
    pass


if __name__ == "__main__":
    main()
