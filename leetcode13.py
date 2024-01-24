#!/usr/bin/env python3

class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        length = len(s)
        i = 0
        while i < length:
            if s[i] == 'I':
                if i + 1 >= length:
                    result += 1
                    i += 1
                elif s[i + 1] == 'V':
                    result += 4
                    i += 2
                elif s[i + 1] == 'X':
                    result += 9
                    i += 2
                else:
                    result += 1
                    i += 1
            elif s[i] == 'X':
                if i + 1 >= length:
                    result += 10
                    i += 1
                elif s[i + 1] == 'L':
                    result += 40
                    i += 2
                elif s[i + 1] == 'C':
                    result += 90
                    i += 2
                else:
                    result += 10
                    i += 1
            elif s[i] == 'C':
                if i + 1 >= length:
                    result += 100
                    i += 1
                elif s[i + 1] == 'D':
                    result += 400
                    i += 2
                elif s[i + 1] == 'M':
                    result += 900
                    i += 2
                else:
                    result += 100
                    i += 1
            elif s[i] == 'V':
                result += 5
                i += 1
            elif s[i] == 'L':
                result += 50
                i += 1
            elif s[i] == 'D':
                result += 500
                i += 1
            elif s[i] == 'M':
                result += 1000
                i += 1
        return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
