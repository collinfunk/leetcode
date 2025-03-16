#!/usr/bin/env python3

def is_prime(value: int) -> bool:
    if value <= 1:
        return False
    if value == 2 or value == 3:
        return True
    if value % 2 == 0 or value % 3 == 0:
        return False
    i = 5
    while i * i <= value:
        if value % i == 0 or value % (i + 2) == 0:
            return False
        i += 6
    return True


def main() -> None:
    result = 0
    for i in range(1, 2000000):
        if is_prime(i):
            result += i
    print(result)


if __name__ == '__main__':
    main()
