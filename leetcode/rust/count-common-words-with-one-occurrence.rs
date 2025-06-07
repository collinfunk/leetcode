// Leetcode problem 2085: Count Common Words With One Occurrence.

use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn count_words(words1: Vec<String>, words2: Vec<String>) -> i32 {
        let table1 = words1.into_iter().fold(HashMap::new(), |mut map, value| {
            *map.entry(value).or_insert(0) += 1;
            map
        });
        let table2 = words2.into_iter().fold(HashMap::new(), |mut map, value| {
            if let Some(1) = table1.get(&value) {
                *map.entry(value).or_insert(0) += 1;
            }
            map
        });
        table2.into_iter().fold(0, |mut acc, key| {
            if key.1 == 1 {
                acc += 1;
            }
            acc
        })
    }
}

fn main() {}
