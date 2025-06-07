// Leetcode problem 2124: Check if All A's Appears Before All B's.

struct Solution {}

impl Solution {
    pub fn check_string(s: String) -> bool {
        let mut found_b = false;
        for ch in s.chars() {
            if ch == 'a' {
                if found_b {
                    return false;
                }
            } else if ch == 'b' {
                found_b = true;
            }
        }
        true
    }
}

fn main() {}
