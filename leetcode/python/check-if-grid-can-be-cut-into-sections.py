#!/usr/bin/env python3

""" Leetcode problem 3394: Check if Grid can be Cut into Sections. """


class Solution:
    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:
        def check_cuts(rectangles: list[list[int]], dim: int) -> bool:
            gap_count = 0
            rectangles.sort(key=lambda x: x[dim])
            furthest_end = rectangles[0][dim + 2]
            for i in range(1, len(rectangles)):
                rectangle = rectangles[i]
                if furthest_end <= rectangle[dim]:
                    gap_count += 1
                furthest_end = max(furthest_end, rectangle[dim + 2])
            return gap_count >= 2
        return check_cuts(rectangles, 0) or check_cuts(rectangles, 1)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
