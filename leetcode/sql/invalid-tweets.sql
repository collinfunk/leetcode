/* Leetcode problem 1683: Invalid Tweets. */

SELECT tweet_id
  FROM Tweets
  WHERE 15 < LENGTH(content);

