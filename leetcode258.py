#!/usr/bin/env python3

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        elif num % 9:
            return 9
        else:
            return num % 9


def main() -> None:
    pass


if __name__ == "__main__":
    main()
