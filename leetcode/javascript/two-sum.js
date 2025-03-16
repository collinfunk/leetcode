/* Leetcode problem 1: Two Sum. */

var twoSum = function (nums, target) {
  let table = new Map();
  for (let i = 0; i < nums.length; ++i) {
    let value = nums[i];
    let need = target - value;
    if (table.has(need)) return [i, table.get(need)];
    table.set(nums[i], i);
  }
  return [];
};
