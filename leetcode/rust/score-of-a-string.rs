// Leetcode problem 3110: Score of a String.

struct Solution {}

impl Solution {
    pub fn score_of_string(s: String) -> i32 {
        s.chars()
            .collect::<Vec<_>>()
            .windows(2)
            .map(|x| (x[1] as i32 - x[0] as i32).abs())
            .sum()
    }
}

fn main() {}
