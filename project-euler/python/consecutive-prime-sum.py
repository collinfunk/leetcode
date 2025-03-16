#!/usr/bin/env python3

import sympy


def main() -> None:
    primes = list(sympy.sieve.primerange(1000000))
    prime_set = set(primes)
    max_value = 0
    max_length = 0
    for i in range(len(primes)):
        current = primes[i]
        for j in range(i + 1, len(primes)):
            current += primes[j]
            if current > primes[-1]:
                continue
            if current in prime_set:
                if max_length < (j - i) + 1:
                    max_value = current
                    max_length = (j - i) + 1
    print(max_value)
    print(max_length)


if __name__ == '__main__':
    main()
