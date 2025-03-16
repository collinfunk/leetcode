#!/usr/bin/env python3

import functools


@functools.lru_cache(maxsize=None)
def fibonacci(value: int) -> int:
    if value == 1 or value == 2:
        return 1
    return fibonacci(value - 1) + fibonacci(value - 2)


def main() -> None:
    i = 1
    while True:
        value = fibonacci(i)
        if len(str(value)) == 1000:
            break
        i += 1
    print(i)


if __name__ == '__main__':
    main()
