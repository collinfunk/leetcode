#!/usr/bin/env python3

""" Leetcode problem 412: Fizz Buzz. """

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            if (i % 3) == 0:
                if (i % 5) == 0:
                    result.append("FizzBuzz")
                else:
                    result.append("Fizz")
            else:
                if (i % 5) == 0:
                    result.append("Buzz")
                else:
                    result.append(str(i))
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
