#!/usr/bin/env python3

from typing import List

""" HankerRank: Grading Students """


def gradingStudents(grades: List[int]) -> List[int]:
    result = []
    for grade in grades:
        if grade >= 38:
            rounded_grade = (grade + 4) - ((grade + 4) % 5)
            if rounded_grade - grade < 3:
                grade = rounded_grade
        result.append(grade)
    return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
