// Leetcode problem 2278: Percentage of Letter in String.

struct Solution {}

impl Solution {
    pub fn percentage_letter(s: String, letter: char) -> i32 {
        let count = s.chars().into_iter().filter(|c| *c == letter).count();
        (count * 100 / s.len() * 100) as i32 / 100
    }
}

fn main() {}
