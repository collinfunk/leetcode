#!/usr/bin/env python3

from typing import List

""" HankerRank: Minimum Distances """


def minimumDistances(a: List[int]) -> int:
    result = -1
    first = dict()
    second = dict()

    for i in range(0, len(a)):
        if first.get(a[i]) is None:
            first[a[i]] = i
        else:
            second[a[i]] = i

    for value in second.keys():
        if second[value] - first[value] < result or result == -1:
            result = second[value] - first[value]

    return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
