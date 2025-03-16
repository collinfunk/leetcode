#!/usr/bin/env python3


def factorial(value: int) -> int:
    if value == 0:
        return 1
    return value * factorial(value - 1)


def main() -> None:
    print(sum([int(x) for x in str(factorial(100))]))


if __name__ == '__main__':
    main()
