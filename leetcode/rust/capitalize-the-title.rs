// Leetcode problem 2129: Capitalize the Title.

struct Solution {}

impl Solution {
    pub fn capitalize_title(title: String) -> String {
        title
            .split_whitespace()
            .map(|word| match word.len() {
                1 | 2 => word.to_ascii_lowercase(),
                _ => word[..1].to_ascii_uppercase() + &word[1..].to_ascii_lowercase(),
            })
            .collect::<Vec<String>>()
            .join(" ")
    }
}

fn main() {}
