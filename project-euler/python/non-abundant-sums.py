#!/usr/bin/env python3

import math


def divisors(value: int) -> list[int]:
    result = []
    square_root = int(math.sqrt(value)) + 1
    for i in range(1, square_root):
        if value % i == 0:
            result.append(i)
            if value // i != i:
                result.append(value // i)
    return sorted(result)


def main() -> None:
    abundant_numbers = []
    for i in range(12, 28124):
        if sum(divisors(i)[:-1]) > i:
            abundant_numbers.append(i)
    abundant_sums = set()
    for number1 in abundant_numbers:
        for number2 in abundant_numbers:
            number_sum = number1 + number2
            if 28123 < number_sum:
                break
            else:
                abundant_sums.add(number_sum)
    print(sum([x for x in range(28124) if x not in abundant_sums]))


if __name__ == '__main__':
    main()
