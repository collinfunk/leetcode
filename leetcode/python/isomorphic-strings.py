#!/usr/bin/env python3

""" Leetcode problem 205: Isomorphic Strings. """


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = dict()
        s_seen = set()
        t_seen = set()
        s_len = len(s)
        t_len = len(t)

        if s_len != t_len:
            return False

        for sc, tc in zip(s, t):
            if sc not in s_seen:
                if tc in t_seen:
                    return False
                mapping[sc] = tc
                s_seen.add(sc)
                t_seen.add(tc)
            else:
                if mapping[sc] != tc:
                    return False

        return True


def main() -> None:
    pass


if __name__ == "__main__":
    main()
