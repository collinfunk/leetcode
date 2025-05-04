/* Leetcode problem 607: Sales Person. */

SELECT MAX(num) as num
  FROM (SELECT num
          FROM MyNumbers
          GROUP BY num
          HAVING COUNT(num) = 1
       ) AS unique_numbers;
