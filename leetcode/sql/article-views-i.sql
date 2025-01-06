/* Leetcode problem 1148: Article Views I. */

SELECT DISTINCT viewer_id AS id
  FROM Views
  WHERE viewer_id = author_id
  ORDER BY viewer_id ASC;

