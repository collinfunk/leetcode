// Leetcode problem 2845: Count of Interesting Subarrays.

use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn count_interesting_subarrays(nums: Vec<i32>, modulo: i32, k: i32) -> i64 {
        let mut table = HashMap::new();
        let mut result = 0;
        let mut prefix = 0;
        *table.entry(0).or_insert(0) += 1;
        for i in 0..nums.len() {
            if nums[i] % modulo == k {
                prefix += 1;
            }
            result += table.get(&((prefix - k + modulo) % modulo)).unwrap_or(&0);
            *table.entry(prefix % modulo).or_insert(0) += 1;
        }
        result
    }
}

fn main() {}
