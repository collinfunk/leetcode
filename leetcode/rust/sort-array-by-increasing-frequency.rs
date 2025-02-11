// Leetcode problem 1636: Sort Array by Increasing Frequency.

use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn frequency_sort(nums: Vec<i32>) -> Vec<i32> {
        let mut values = nums.clone();
        let mut table = HashMap::new();
        values.sort_by(|a, b| b.cmp(a));
        for value in values.iter() {
            *table.entry(value).or_insert(0) += 1;
        }
        let mut result = values.clone();
        result.sort_unstable_by_key(|x| (table[x], -(*x)));
        result
    }
}

fn main() {}
