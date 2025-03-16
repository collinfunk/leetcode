#!/usr/bin/env python3

import sympy


def permute(n: int) -> list[int]:
    result: list[str] = []
    digits = [str(x) for x in range(1, n + 1)]

    def visit(result: list[str], array: list[str], index: int) -> None:
        if index == len(array):
            result.append(array[:])
            return
        for i in range(index, len(array)):
            array[index], array[i] = array[i], array[index]
            visit(result, array, index + 1)
            array[index], array[i] = array[i], array[index]

    visit(result, digits, 0)
    return [int(''.join(x)) for x in result]


def main() -> None:
    result = 0
    for i in range(1, 10):
        values = permute(i)
        for value in values:
            if sympy.isprime(value):
                if result < value:
                    result = value
    print(result)


if __name__ == '__main__':
    main()
