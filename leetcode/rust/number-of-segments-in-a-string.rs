// Leetcode problem 434: Number of Segments in a String.

struct Solution {}

impl Solution {
    pub fn count_segments(s: String) -> i32 {
        s.split_ascii_whitespace().count() as i32
    }
}

fn main() {}
