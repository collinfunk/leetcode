#!/usr/bin/env python3


def factorial(value: int) -> int:
    if value == 0:
        return 1
    return value * factorial(value - 1)


def main() -> None:
    print(factorial(40) // factorial(20) ** 2)


if __name__ == '__main__':
    main()
