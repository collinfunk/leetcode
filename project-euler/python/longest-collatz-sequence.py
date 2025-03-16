#!/usr/bin/env python3

def collatz_function(value: int) -> int:
    if value % 2 == 0:
        return value / 2
    return 3 * value + 1


def main() -> None:
    result = 0
    maximum_length = 0
    for i in range(2, 1000000):
        value = i
        length = 0
        while value != 1:
            value = collatz_function(value)
            length += 1
        if maximum_length < length:
            maximum_length = length
            result = i
    print(maximum_length)
    print(result)


if __name__ == '__main__':
    main()
