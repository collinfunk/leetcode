#!/usr/bin/env python3

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n and not (n & (n - 1))


def main() -> None:
    pass


if __name__ == "__main__":
    main()
