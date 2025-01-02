/* Leetcode problem 577: Employee Bonus. */

SELECT x.name, y.bonus
  FROM Employee x
  LEFT JOIN Bonus y
  ON x.empId = y.empId
  WHERE y.bonus IS NULL
  OR y.bonus < 1000;
