#!/usr/bin/env python3


def main() -> None:
    result = 1
    for i in range(10, 100):
        i_tenths = i // 10
        i_ones = i % 10
        for j in range(i, 100):
            j_tenths = j // 10
            j_ones = j % 10
            if i_ones == j_tenths and j_ones != 0 and i_tenths != j_ones and i_tenths / j_ones == i / j:
                result *= i / j
    print(round(result, 2))


if __name__ == '__main__':
    main()
