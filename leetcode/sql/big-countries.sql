/* Leetcode problem 595: Big Countries. */

SELECT name, population, area
  FROM World
  WHERE 3000000 <= area
  OR 25000000 <= population;

