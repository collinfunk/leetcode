#!/usr/bin/env python3

""" Leetcode problem 682: Baseball Game. """


class Solution:
    def calPoints(self, operations: list[str]) -> int:
        scores = []
        for operation in operations:
            if operation == 'C':
                scores.pop()
            elif operation == 'D':
                scores.append(scores[-1] * 2)
            elif operation == '+':
                scores.append(scores[-1] + scores[-2])
            else:
                scores.append(int(operation))
        return sum(scores)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
