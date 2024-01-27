#!/usr/bin/env python3

""" Leetcode problem 190: Reverse Bits. """


class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(0, 32):
            result = result << 1
            result |= n & 1
            n = n >> 1
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
