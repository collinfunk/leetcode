#!/usr/bin/env python3

import math


def divisors(value: int) -> list[int]:
    result = []
    square_root = int(math.sqrt(value)) + 1
    for i in range(1, square_root):
        if value % i == 0:
            result.append(i)
            if value // i != i:
                result.append(value // i)
    return sorted(result)


def triangle_number(value: int):
    return value * (value + 1) // 2


def main() -> None:
    i = 1
    result = 0
    while True:
        result = triangle_number(i)
        if 500 < len(divisors(result)):
            break
        i += 1
    print(result)


if __name__ == '__main__':
    main()
