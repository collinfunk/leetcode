// Leetcode problem 1374: Generate a String With Characters That Have Odd Counts.

struct Solution {}

impl Solution {
    pub fn generate_the_string(n: i32) -> String {
        "a".repeat((n - 1 + (n & 1)) as usize) + &"b".repeat((1 - (n & 1)) as usize)
    }
}

fn main() {}
