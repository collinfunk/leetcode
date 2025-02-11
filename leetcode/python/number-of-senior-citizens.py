#!/usr/bin/env python3

""" Leetcode problem 2678: Number of Senior Citizens. """


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        result = 0
        for person in details:
            age = int(person[11:13])
            if 60 < age:
                result += 1
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
