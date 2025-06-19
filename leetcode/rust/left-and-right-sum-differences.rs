// Leetcode problem 2574: Left and Right Sum Differences.

struct Solution {}

impl Solution {
    pub fn left_right_difference(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut left = 0;
        let mut right = nums.iter().sum::<i32>();
        let mut prev = 0;
        let mut result = vec![0; n];
        for i in 0..n {
            right -= nums[i];
            left += prev;
            prev = nums[i];
            result[i] = (left - right).abs();
        }
        result
    }
}

fn main() {}
