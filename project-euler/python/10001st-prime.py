#!/usr/bin/env python3

def is_prime(value: int) -> bool:
    divisor = 3
    square = divisor * divisor
    while square < value and value % divisor != 0:
        divisor += 1
        square += 4 * divisor
        divisor += 1
    return value % divisor


def main() -> None:
    current_prime = 3
    count = 1

    while True:
        if count == 10001 - 1:
            break
        current_prime += 2
        if is_prime(current_prime):
            count += 1
    print(current_prime)


if __name__ == '__main__':
    main()
