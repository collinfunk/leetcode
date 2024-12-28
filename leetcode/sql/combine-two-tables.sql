/* Leetcode problem 175: Combine Two Tables. */

SELECT x.firstName, x.lastName, y.city, y.state
  FROM Person x
  LEFT JOIN Address y
  ON x.personId = y.personId;
