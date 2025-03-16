#!/usr/bin/env python3

def main() -> None:
    result = 0
    table = ["" for i in range(0, 91)]
    table[1] = "one"
    table[2] = "two"
    table[3] = "three"
    table[4] = "four"
    table[5] = "five"
    table[6] = "six"
    table[7] = "seven"
    table[8] = "eight"
    table[9] = "nine"
    table[10] = "ten"
    table[11] = "eleven"
    table[12] = "twelve"
    table[13] = "thirteen"
    table[14] = "fourteen"
    table[15] = "fifteen"
    table[16] = "sixteen"
    table[17] = "seventeen"
    table[18] = "eighteen"
    table[19] = "nineteen"
    table[20] = "twenty"
    table[30] = "thirty"
    table[40] = "forty"
    table[50] = "fifty"
    table[60] = "sixty"
    table[70] = "seventy"
    table[80] = "eighty"
    table[90] = "ninety"
    for i in range(1, 1001):
        value = i
        english = ""
        if value == 1000:
            english += 'onethousand'
            value = 0
        if value >= 100:
            english += table[value // 100] + 'hundred'
            value = value % 100
            if value != 0:
                english += 'and'
        if value >= 20:
            english += table[value - value % 10]
            value = value % 10
        if value != 0:
            english += table[value]
        print(f'{i} {english}')
        result += len(english)

    print(result)


if __name__ == '__main__':
    main()
