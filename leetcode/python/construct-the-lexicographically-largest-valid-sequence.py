#!/usr/bin/env python3

""" Leetcode problem 1718: Construct the Lexicographically Largest Valid Sequence. """


class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        result = [0] * (n + n - 1)
        unseen = set(range(1, n + 1))

        def backtrack(index: int) -> bool:
            if not unseen:
                return True
            if result[index]:
                return backtrack(index + 1)
            for value in reversed(range(1, n + 1)):
                index2 = index + value if value != 1 else index
                if value in unseen and index2 < n + n - 1 and not result[index2]:
                    result[index] = value
                    result[index2] = value
                    unseen.remove(value)
                    if backtrack(index + 1):
                        return True
                    result[index] = 0
                    result[index2] = 0
                    unseen.add(value)
            return False
        backtrack(0)
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
