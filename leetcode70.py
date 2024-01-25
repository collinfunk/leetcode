#!/usr/bin/env python3

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        x = 1
        y = 2
        result = 0

        for i in range(2, n):
            result = x + y
            x = y
            y = result

        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
