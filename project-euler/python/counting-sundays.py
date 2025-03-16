#!/usr/bin/env python3

days_per_month = [
    31,  # January
    28,  # February (non-leap year)
    31,  # March
    30,  # April
    31,  # May
    30,  # June
    31,  # July
    31,  # August
    30,  # September
    31,  # October
    30,  # November
    31,  # December
]

table_of_month_offsets = [
    [0, 0],  # January
    [3, 3],  # February
    [3, 4],  # March
    [6, 0],  # April
    [1, 2],  # May
    [4, 5],  # June
    [6, 0],  # July
    [2, 3],  # August
    [5, 6],  # September
    [0, 1],  # October
    [3, 4],  # November
    [5, 6],  # December
]


def is_leap_year(year: int) -> bool:
    return ((year) % 4 == 0 and ((year) % 100 != 0 or (year) % 400 == 0))


def main() -> None:
    result = 0
    for year in range(1901, 2001):
        january_1 = (1 + 5 * ((year - 1) % 4) + 4 * ((year - 1) %
                     100) + 6 * ((year - 1) % 400)) % 7
        for month in range(0, 12):
            month_offset = table_of_month_offsets[month][is_leap_year(year)]
            if (january_1 + month_offset + 1) % 7 == 1:
                result += 1
    print(result)


if __name__ == '__main__':
    main()
