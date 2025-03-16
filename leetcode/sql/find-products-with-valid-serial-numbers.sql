/* Leetcode problem 3465: Find Products with Valid Serial Numbers. */

SELECT product_id, product_name, description
  FROM products
  WHERE description REGEXP 'SN[0-9]{4}-[0-9]{4}([^0-9]|$)'
  ORDER BY product_id;
