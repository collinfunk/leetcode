
/* Leetcode problem 2626: Array Reduce Transformation. */

/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
  let result = init;
  for (let i = 0; i < nums.length; ++i) {
    if (i === 0) {
      result = fn(init, nums[i]);
    } else {
      result = fn(result, nums[i]);
    }
  }
  return result;
};
