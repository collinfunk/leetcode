#!/usr/bin/env python3


def main() -> None:
    numbers = [i for i in range(2, 21)]
    value = 20
    while True:
        found = True
        for number in numbers:
            if value % number != 0:
                value += numbers[-1]
                found = False
            if not found:
                break
        if found:
            break
    print(value)


if __name__ == '__main__':
    main()
