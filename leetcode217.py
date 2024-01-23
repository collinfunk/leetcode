#!/usr/bin/env python3

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen_values = set()

        for value in nums:
            if value in seen_values:
                return True
            else:
                seen_values.add(value)

        return False


def main() -> None:
    pass


if __name__ == "__main__":
    main()
