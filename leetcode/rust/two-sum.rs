/* Leetcode problem 1: Two Sum. */

use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut table = HashMap::new();

        for (i, &num) in nums.iter().enumerate() {
            let need = target - num;
            if let Some(&need_index) = table.get(&need) {
                return vec![need_index as i32, i as i32];
            }
            table.insert(num, i);
        }
        vec![]
    }
}

fn main() {}
