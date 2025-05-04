// Leetcode problem 961: N-Repeated Element in Size 2N Array.

use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn repeated_n_times(nums: Vec<i32>) -> i32 {
        let n = nums.len() / 2;
        let mut table = HashMap::new();
        for num in nums {
            table
                .entry(num)
                .and_modify(|count| *count += 1)
                .or_insert(1);
            if table[&num] == n {
                return num;
            }
        }
        -1
    }
}

fn main() {}
