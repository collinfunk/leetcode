/* Leetcode problem 1068: Product Sales Analysis I. */

SELECT y.product_name, x.year, x.price
  FROM Sales x
  JOIN Product y
  on x.product_id = y.product_id;
