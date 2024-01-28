
/* Leetcode problem 1: Two Sum. */

function twoSum(nums: number[], target: number): number[] {
  const table = new Map()
  for (let i = 0; i < nums.length; ++i) {
    const value = nums[i]
    const need = target - value
    if (table.has(need))
      return [i, table.get(need)]
    table.set(nums[i], i)
  }
  return []
};
