/* Leetcode problem 1075: Project Employees I. */

SELECT project_id, ROUND(AVG(experience_years), 2) AS average_years
  FROM Project x
  JOIN Employee y
  ON x.employee_id = y.employee_id
  GROUP BY project_id;
