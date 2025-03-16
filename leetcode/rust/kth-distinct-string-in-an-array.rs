// Leetcode problem 2053: Kth Distinct String in an Array.

use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn kth_distinct(arr: Vec<String>, k: i32) -> String {
        let table = arr.clone().into_iter().fold(HashMap::new(), |mut map, x| {
            *map.entry(x).or_insert(0) += 1;
            map
        });
        let mut i = 0;
        for entry in arr {
            if table.get(&entry) == Some(&1) {
                i += 1;
                if i == k {
                    return entry;
                }
            }
        }
        "".to_string()
    }
}

fn main() {}
