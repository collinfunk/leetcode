/* Leetcode problem 1581: Customer Who Visited but Did Not Make Any Transactions. */

SELECT x.customer_id, COUNT(x.visit_id) AS count_no_trans
  FROM Visits x
  LEFT JOIN Transactions y
  ON x.visit_id = y.visit_id
  WHERE y.transaction_id IS NULL
  GROUP BY x.customer_id;
