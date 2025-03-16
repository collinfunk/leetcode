#!/usr/bin/env python3

import itertools


def main() -> None:
    print(''.join(list(itertools.permutations('0123456789', 10))[999999]))


if __name__ == '__main__':
    main()
