// Leetcode problem 2220: Minimum Bit Flips to Convert Number.

struct Solution {}

impl Solution {
    pub fn min_bit_flips(start: i32, goal: i32) -> i32 {
        (start ^ goal).count_ones() as i32
    }
}

fn main() {}
