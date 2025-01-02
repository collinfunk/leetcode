/* Leetcode problem 181: Employees Earning More Than Their Managers. */

SELECT x.name
  AS Employee
  FROM Employee x
  INNER JOIN Employee y
  WHERE x.managerId = y.id
  AND x.salary > y.salary;

