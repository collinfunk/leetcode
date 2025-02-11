#!/usr/bin/env python3

""" Leetcode problem 506: Relative Ranks. """


class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        table = {score[i]: i for i in range(len(score))}
        score.sort(reverse=True)
        result = ["" for _ in range(len(score))]
        for i in range(len(score)):
            if i == 0:
                result[table[score[i]]] = "Gold Medal"
            elif i == 1:
                result[table[score[i]]] = "Silver Medal"
            elif i == 2:
                result[table[score[i]]] = "Bronze Medal"
            else:
                result[table[score[i]]] = str(i + 1)
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
