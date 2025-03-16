// Leetcode problem 1480: Running Sum of 1d Array.

struct Solution {}

impl Solution {
    pub fn running_sum(nums: Vec<i32>) -> Vec<i32> {
        let mut acc = 0;
        let mut result = Vec::new();
        for (i, num) in nums.iter().enumerate() {
            acc += num;
            result.push(acc);
        }
        result
    }
}

fn main() {}
