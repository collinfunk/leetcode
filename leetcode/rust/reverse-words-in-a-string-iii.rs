// Leetcode problem 557: Reverse Words in a String III.

struct Solution {}

impl Solution {
    pub fn reverse_words(s: String) -> String {
        s.split(" ")
            .map(|x| x.chars().rev().collect())
            .collect::<Vec<String>>()
            .join(" ")
    }
}

fn main() {}
