/* Leetcode problem 627: Swap Salary. */

UPDATE Salary
  SET sex = CASE
              WHEN sex = 'm' THEN 'f'
              WHEN sex = 'f' THEN 'm'
              ELSE sex
            END
  WHERE sex in ('m', 'f');

