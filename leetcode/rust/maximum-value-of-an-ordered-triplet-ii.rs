// Leetcode problem 2874: Maximum Value of an Ordered Triplet II.

struct Solution {}

impl Solution {
    pub fn maximum_triplet_value(nums: Vec<i32>) -> i64 {
        let mut result = 0;
        let mut value1 = 0;
        let mut value2 = 0;
        for i in 0..nums.len() {
            result = result.max(value1 * nums[i] as i64);
            value1 = value1.max(value2 - nums[i] as i64);
            value2 = value2.max(nums[i] as i64);
        }
        result
    }
}

fn main() {}
