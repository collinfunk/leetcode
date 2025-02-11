// Leetcode problem 1913: Maximum Product Difference Between Two Pairs.

struct Solution {}

impl Solution {
    pub fn max_product_difference(nums: Vec<i32>) -> i32 {
        let mut sorted_nums = nums.clone();
        sorted_nums.sort_unstable();
        sorted_nums[sorted_nums.len() - 1] * sorted_nums[sorted_nums.len() - 2]
            - sorted_nums[0] * sorted_nums[1]
    }
}

fn main() {}
