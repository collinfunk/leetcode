#!/usr/bin/env python3

""" Leetcode problem 2818: Apply Operations to Maximize Score. """

from collections import deque


class Solution:
    MOD = int(1e9 + 7)

    def maximumScore(self, nums: list[int], k: int) -> int:
        def power(base: int, exponent: int) -> int:
            result = 1
            while exponent > 0:
                if exponent % 2:
                    result = (result * base) % self.MOD
                base = (base * base) % self.MOD
                exponent //= 2
            return result
        max_element = max(nums)
        is_prime = [True] * (max_element + 1)
        primes = []
        for i in range(2, max_element + 1):
            if not is_prime[i]:
                continue
            primes.append(i)
            for multiple in range(i * i, max_element + 1, i):
                is_prime[multiple] = False
        n = len(nums)
        prime_scores = [0] * n
        for i in range(n):
            num = nums[i]
            for prime in primes:
                if num < prime * prime:
                    break
                if num % prime != 0:
                    continue
                prime_scores[i] += 1
                while num % prime == 0:
                    num //= prime
            if num > 1:
                prime_scores[i] += 1
        next_dominant = [n] * n
        prev_dominant = [-1] * n
        decreasing_prime_score = deque()
        for i in range(n):
            while decreasing_prime_score and prime_scores[decreasing_prime_score[-1]] < prime_scores[i]:
                top_index = decreasing_prime_score.pop()
                next_dominant[top_index] = i
            if decreasing_prime_score:
                prev_dominant[i] = decreasing_prime_score[-1]
            decreasing_prime_score.append(i)
        number_of_subarrays = [(next_dominant[i] - i)
                               * (i - prev_dominant[i]) for i in range(n)]
        sorted_array = sorted(enumerate(nums), key=lambda x: -x[1])
        result = 1
        i = 0
        while k > 0:
            index, num = sorted_array[i]
            i += 1
            operations = min(k, number_of_subarrays[index])
            result = (result * power(num, operations)) % self.MOD
            k -= operations
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
