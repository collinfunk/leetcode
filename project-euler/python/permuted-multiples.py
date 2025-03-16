#!/usr/bin/env python3

from collections import defaultdict


def is_permutation(value1: int, value2: int) -> bool:
    if value1 == value2:
        return False
    str1 = str(value1)
    str2 = str(value2)
    table = defaultdict(int)
    for ch in str1:
        table[ch] += 1
    for ch in str2:
        table[ch] -= 1
    for value in table.values():
        if value != 0:
            return False
    return True


def main() -> None:
    i = 1
    while True:
        values = [i * x for x in range(2, 7)]
        found = True
        for value in values:
            if not is_permutation(i, value):
                found = False
                break
        if found:
            break
        i += 1
    print(i)


if __name__ == '__main__':
    main()
