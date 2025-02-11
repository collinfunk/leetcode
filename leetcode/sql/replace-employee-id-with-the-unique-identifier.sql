/* Leetcode problem 1378: Replace Employee ID With The Unique Identifier. */

SELECT y.unique_id, x.name
  FROM Employees x
  LEFT JOIN EmployeeUNI y
  ON x.id = y.id;
