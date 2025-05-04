// Leetcode problem 3512: Minimum Operations to Make Array Sum Divisible by K.

struct Solution {}

impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        let nums_sum = nums.into_iter().fold(0, |acc, x| acc + x);
        nums_sum % k
    }
}

fn main() {}
