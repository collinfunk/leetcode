// Leetcode problem 1528: Shuffle String.

struct Solution {}

impl Solution {
    pub fn restore_string(s: String, indices: Vec<i32>) -> String {
        let mut result = vec![' '; s.len()];
        for (i, ch) in s.chars().enumerate() {
            result[indices[i] as usize] = ch;
        }
        result.into_iter().collect()
    }
}

fn main() {}
