// Leetcode problem 1128: Number of Equivalent Domino Pairs.

use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn num_equiv_domino_pairs(dominoes: Vec<Vec<i32>>) -> i32 {
        let table = dominoes.iter().fold(HashMap::new(), |mut map, x| {
            *map.entry((x[0].min(x[1]), x[0].max(x[1]))).or_insert(0) += 1;
            map
        });
        table.values().map(|x| (x * (x - 1)) / 2).sum()
    }
}

fn main() {}
