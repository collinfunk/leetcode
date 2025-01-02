/* Leetcode problem 197: Rising Temperature. */

SELECT x.id
  FROM Weather x
  JOIN Weather y
  ON DATEDIFF(x.recordDate, y.recordDate) = 1
  WHERE x.temperature > y.temperature;
