// Leetcode problem 1748: Sum of Unique Elements.

use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn sum_of_unique(nums: Vec<i32>) -> i32 {
        let table = nums.clone().into_iter().fold(HashMap::new(), |mut map, x| {
            *map.entry(x).or_insert(0) += 1;
            map
        });
        nums.into_iter().fold(0, |acc, x| {
            acc + if table.get(&x) == Some(&1) { x } else { 0 }
        })
    }
}

fn main() {}
