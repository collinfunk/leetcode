
/* Leetcode problem 2727: Is Object Empty. */

/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
  for (const property in obj) {
    if (Object.hasOwn(obj, property)) {
      return false;
    }
  }
  return true;
};
