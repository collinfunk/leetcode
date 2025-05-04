// Leetcode problem 3467: Transform Array by Parity.

struct Solution {}

impl Solution {
    pub fn transform_array(nums: Vec<i32>) -> Vec<i32> {
        let mut result = nums.into_iter().map(|x| x % 2).collect::<Vec<_>>();
        result.sort_unstable();
        result
    }
}

fn main() {}
