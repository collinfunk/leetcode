#!/usr/bin/env python3


def main() -> None:
    data = ""
    with open('0022_names.txt', 'r', encoding='utf-8') as stream:
        data = stream.read()
    names = sorted([name.replace('"', '') for name in data.split(',"')])
    result = 0
    for i, name in enumerate(names):
        worth = sum([(ord(x) - ord('A')) + 1 for x in name])
        result += (i + 1) * worth
    print(result)


if __name__ == '__main__':
    main()
