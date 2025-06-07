// Leetcode problem 2900: Longest Unequal Adjacent Groups Subsequence I.

struct Solution {}

impl Solution {
    pub fn get_longest_subsequence(words: Vec<String>, groups: Vec<i32>) -> Vec<String> {
        let mut result = Vec::new();
        for i in 0..words.len() {
            if i == 0 || groups[i] != groups[i - 1] {
                result.push(words[i].clone())
            }
        }
        result
    }
}

fn main() {}
