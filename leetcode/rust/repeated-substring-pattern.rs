// Leetcode problem 459: Repeated Substring Pattern.

struct Solution {}

impl Solution {
    pub fn repeated_substring_pattern(s: String) -> bool {
        let double = s.clone() + &s;
        let sub = &double[1..double.len() - 1];
        sub.contains(&s)
    }
}

fn main() {}
