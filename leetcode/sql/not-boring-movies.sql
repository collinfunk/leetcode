/* Leetcode problem 620: Not Boring Movies. */

SELECT *
  FROM Cinema
  WHERE id % 2 != 0 and description != "boring"
  ORDER BY rating DESC;
