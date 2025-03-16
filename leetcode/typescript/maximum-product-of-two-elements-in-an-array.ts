/* Leetcode problem 1464: Maximum Product of Two Elements in an Array. */

function maxProduct(nums: number[]): number {
  nums = nums.sort((a, b) => a - b);
  return (nums.at(-1) - 1) * (nums.at(-2) - 1);
}
