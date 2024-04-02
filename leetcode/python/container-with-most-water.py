#!/usr/bin/env python3

""" Leetcode problem 11: Container With Most Water. """


class Solution:
    def maxArea(self, height: list[int]) -> int:
        start = 0
        end = len(height) - 1
        max_area = 0
        while start < end:
            current = (end - start) * min(height[start], height[end])
            max_area = max(max_area, current)

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return max_area


def main() -> None:
    pass


if __name__ == "__main__":
    main()
