// Leetcode problem 1486: XOR Operation in an Array.

struct Solution {}

impl Solution {
    pub fn xor_operation(n: i32, start: i32) -> i32 {
        (1..n).fold(start, |acc, x| acc ^ (start + 2 * x))
    }
}

fn main() {}
