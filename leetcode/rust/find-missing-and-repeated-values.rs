// Leetcode problem 2965: Find Missing and Repeated Values.

use std::collections::HashSet;

struct Solution {}

impl Solution {
    pub fn find_missing_and_repeated_values(grid: Vec<Vec<i32>>) -> Vec<i32> {
        let mut seen: HashSet<i32> = HashSet::new();
        let mut a = 0;
        let mut b = 0;
        for row in &grid {
            for entry in row {
                if seen.contains(&entry) {
                    a = *entry;
                } else {
                    seen.insert(*entry);
                }
            }
        }
        for i in 1..=grid.len() * grid.len() {
            if !seen.contains(&(i as i32)) {
                b = i as i32;
                break;
            }
        }
        [a, b].to_vec()
    }
}

fn main() {}
