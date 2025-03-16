// Leetcode problem 2460: Apply Operations to an Array.

struct Solution {}

impl Solution {
    pub fn apply_operations(nums: Vec<i32>) -> Vec<i32> {
        let mut result = nums.clone();
        for i in 0..result.len() - 1 {
            if result[i] == result[i + 1] {
                result[i] <<= 1;
                result[i + 1] = 0;
            }
        }
        let mut j = 0;
        for i in 0..result.len() {
            if result[i] != 0 {
                result[j] = result[i];
                j += 1;
            }
        }
        while j < result.len() {
            result[j] = 0;
            j += 1;
        }
        result
    }
}

fn main() {}
