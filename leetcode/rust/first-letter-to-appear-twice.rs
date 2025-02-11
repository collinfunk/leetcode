// Leetcode problem 2351: First Letter to Appear Twice.

struct Solution {}

impl Solution {
    pub fn repeated_character(s: String) -> char {
        let mut table = [0; 255];
        for character in s.bytes() {
            table[character as usize] += 1;
            if table[character as usize] == 2 {
                return character as char;
            }
        }
        unreachable!();
    }
}

fn main() {}
