// Leetcode problem 1863: Sum of All Subset XOR Totals.

struct Solution {}

impl Solution {
    pub fn subset_xor_sum(nums: Vec<i32>) -> i32 {
        nums.iter().fold(0, |acc, x| acc | x) << (nums.len() - 1)
    }
}

fn main() {}
