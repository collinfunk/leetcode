#!/usr/bin/env python3

import math


def main() -> None:
    a = 1
    b = 0
    c = 0
    found = False
    while True:
        b = a
        while True:
            c = math.sqrt((a ** 2) + (b ** 2))
            if a + b + c > 1000:
                break
            if c.is_integer() and int(c) + a + b == 1000:
                c = int(c)
                found = True
                break
            b += 1
        if found:
            break
        a += 1
    print(a * b * c)


if __name__ == '__main__':
    main()
