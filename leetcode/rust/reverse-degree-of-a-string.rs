// Leetcode problem 3498: Reverse Degree of a String.

struct Solution {}

impl Solution {
    pub fn reverse_degree(s: String) -> i32 {
        s.bytes().enumerate().fold(0, |acc, (i, x)| {
            acc + ((((b'z' - x) as i32) + 1) * (i as i32 + 1))
        })
    }
}

fn main() {}
