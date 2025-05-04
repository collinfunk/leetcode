// Leetcode problem 3427: Sum of Variable Length Subarrays.

struct Solution {}

impl Solution {
    pub fn subarray_sum(nums: Vec<i32>) -> i32 {
        let mut result = 0;
        for i in 0..nums.len() {
            let start = (i as i32 - nums[i]).max(0);
            result += &nums[(start as usize)..i + 1].iter().sum();
        }
        result
    }
}

fn main() {}
