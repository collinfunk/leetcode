/* Leetcode problem 584: Find Customer Referee. */

SELECT x.name
  FROM Customer x
  WHERE x.referee_id != 2 or x.referee_id IS NULL;
