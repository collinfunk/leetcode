// Leetcode problem 2206: Divide Array Into Equal Pairs.

use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn divide_array(nums: Vec<i32>) -> bool {
        let table = nums.into_iter().fold(HashMap::new(), |mut map, value| {
            *map.entry(value).or_insert(0) += 1;
            map
        });
        for (_, count) in table {
            if count % 2 != 0 {
                return false;
            }
        }
        true
    }
}

fn main() {}
