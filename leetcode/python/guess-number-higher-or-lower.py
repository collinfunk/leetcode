#!/usr/bin/env python3

""" Leetcode problem 374: Guess Number Higher or Lower. """


def guess(num: int) -> int:
    """ Stub function defined by leetcode. """
    return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while (low <= high):
            mid = low + (high - low) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == -1:
                high = mid - 1
            elif result == 1:
                low = mid + 1
        return -1


def main() -> None:
    pass


if __name__ == "__main__":
    main()
