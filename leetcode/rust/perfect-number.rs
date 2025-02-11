// Leetcode problem 507: Perfect Number.

use std::collections::HashSet;

struct Solution {}

impl Solution {
    pub fn check_perfect_number(num: i32) -> bool {
        HashSet::from([6, 28, 496, 8128, 33550336])
            .get(&num)
            .is_some()
    }
}

fn main() {}
