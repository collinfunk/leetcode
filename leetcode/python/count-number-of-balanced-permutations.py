#!/usr/bin/env python3

""" Leetcode problem 3343: Count Number of Balanced Permutations. """

import functools
import math
from collections import Counter


class Solution:

    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10**9 + 7
        num_list = list(map(int, num))
        total = sum(num_list)
        if total % 2 != 0:
            return 0
        target = total // 2
        counter = Counter(num_list)
        n = len(num_list)
        max_odd = (n + 1) // 2
        psum = [0] * 11
        for i in range(9, -1, -1):
            psum[i] = psum[i + 1] + counter[i]

        @functools.lru_cache(maxsize=None)
        def dfs(pos: int, curr: int, odd_count: int):
            if odd_count < 0 or psum[pos] < odd_count or curr > target:
                return 0
            if pos > 9:
                return int(curr == target and odd_count == 0)
            even_count = psum[pos] - odd_count
            result = 0
            for i in range(max(0, counter[pos] - even_count), min(counter[pos], odd_count) + 1):
                ways = math.comb(odd_count, i) * \
                    math.comb(even_count, counter[pos] - i) % MOD
                result += ways * dfs(pos + 1, curr + i * pos, odd_count - i)
            return result % MOD

        return dfs(0, 0, max_odd)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
