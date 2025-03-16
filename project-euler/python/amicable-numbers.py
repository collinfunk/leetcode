#!/usr/bin/env python3

def d(n: int) -> int:
    result = 0
    for i in range(1, n):
        if n % i == 0:
            result += i
    return result


def main() -> None:
    result = 0
    for i in range(10000):
        result1 = d(i)
        if d(result1) == i and i != result1:
            result += i
    print(result)


if __name__ == '__main__':
    main()
