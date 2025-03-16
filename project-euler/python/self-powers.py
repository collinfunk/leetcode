#!/usr/bin/env python3

def main() -> None:
    result = 0
    for i in range(1, 1001):
        result += i ** i
    print(str(result)[len(str(result)) - 10:])


if __name__ == '__main__':
    main()
