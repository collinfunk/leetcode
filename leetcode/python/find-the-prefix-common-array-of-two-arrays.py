#!/usr/bin/env python3

""" Leetcode problem 2657: Find the Prefix Common Array of Two Arrays. """


from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        table_a = set()
        table_b = set()
        result = []
        count = 0
        for i in range(0, len(A)):
            table_a.add(A[i])
            table_b.add(B[i])
            if A[i] == B[i]:
                count += 1
            else:
                if A[i] in table_b:
                    count += 1
                if B[i] in table_a:
                    count += 1
            result.append(count)
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
