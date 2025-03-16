#!/usr/bin/env python3

def is_palindromic(value: int) -> None:
    return str(value) == str(value)[::-1]


def main() -> None:
    value = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            if is_palindromic(i * j):
                if value < i * j:
                    value = i * j
    print(value)


if __name__ == '__main__':
    main()
