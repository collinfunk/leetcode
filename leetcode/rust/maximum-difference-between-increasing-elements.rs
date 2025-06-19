// Leetcode problem 2016: Maximum Difference Between Increasing Elements.

struct Solution {}

impl Solution {
    pub fn maximum_difference(nums: Vec<i32>) -> i32 {
        let mut result = -1;
        let mut max = nums[0];
        let mut min = nums[0];
        for &value in &nums[1..] {
            if value < min {
                min = value;
                max = value;
            } else if max < value {
                max = value;
                result = result.max(max - min);
            }
        }
        result
    }
}

fn main() {}
