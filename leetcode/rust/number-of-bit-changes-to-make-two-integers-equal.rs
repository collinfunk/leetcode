// Leetcode problem 3226: Number of Bit Changes to Make Two Integers Equal.

struct Solution {}

impl Solution {
    pub fn min_changes(n: i32, k: i32) -> i32 {
        if k & !n > 0 {
            -1
        } else {
            (n & !k).count_ones() as i32
        }
    }
}

fn main() {}
