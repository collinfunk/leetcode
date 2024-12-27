/* Leetcode problem 196: Delete Duplicate Emails. */

DELETE x from person x, person2 y WHERE x.email = y.email AND x.id > y.id;
