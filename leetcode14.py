#!/usr/bin/env python3

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = min(strs, key=len)
        for s in strs:
            if len(result) > 0:
                if s.startswith(result):
                    break
                else:
                    result = result[:-1]
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
