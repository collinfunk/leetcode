// Leetcode problem 3375: Minimum Operations to Make Array Values Equal to K.

use std::collections::HashSet;

struct Solution {}

impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        let mut table = HashSet::new();
        for num in nums {
            if num < k {
                return -1;
            }
            if k < num {
                table.insert(num);
            }
        }
        table.len() as i32
    }
}

fn main() {}
