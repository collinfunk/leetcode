#!/usr/bin/env python3

class Solution:
    def isHappy(self, n: int) -> bool:
        values = set()
        while n != 1 and n not in values:
            values.add(n)
            n = sum(int(i) ** 2 for i in str(n))
        return n == 1


def main() -> None:
    pass


if __name__ == "__main__":
    main()
