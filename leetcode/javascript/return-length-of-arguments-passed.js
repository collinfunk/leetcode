/* Leetcode problem 2703: Return Length of Arguments Passed. */


/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function() {
  return arguments.length;
};

/**
 * argumentsLength(1, 2, 3); // 3
 */
