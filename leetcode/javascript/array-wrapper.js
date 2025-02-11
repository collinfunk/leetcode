/* Leetcode problem 2695: Array Wrapper. */

/**
 * @param {number[]} nums
 * @return {void}
 */
var ArrayWrapper = function(nums) {
  this.nums = nums;
};

/**
 * @return {number}
 */
ArrayWrapper.prototype.valueOf = function() {
  return this.nums.reduce((a, b) => a + b, 0);
}

/**
 * @return {string}
 */
ArrayWrapper.prototype.toString = function() {
  if (this.nums.length === 0) {
    return '[]';
  } else if (this.nums.length === 1) {
    return `[${this.nums[0]}]`
  } else {
    let result = '[';
    for (let i = 0; i < this.nums.length; ++i) {
      if (i === this.nums.length - 1) {
        result += `${this.nums[i]}]`
      } else {
        result += `${this.nums[i]},`
      }
    }
    return result;
  }
}

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */
