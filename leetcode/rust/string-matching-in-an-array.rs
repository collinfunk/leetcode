// Leetcode problem 1408: String Matching in an Array.

use std::collections::HashSet;

struct Solution {}

impl Solution {
    pub fn string_matching(words: Vec<String>) -> Vec<String> {
        let mut result = HashSet::new();
        for i in 0..words.len() - 1 {
            for j in i + 1..words.len() {
                if words[i].len() < words[j].len() {
                    if words[j].contains(&words[i]) {
                        result.insert(words[i].clone());
                    }
                } else {
                    if words[i].contains(&words[j]) {
                        result.insert(words[j].clone());
                    }
                }
            }
        }
        result.iter().map(|x| x.to_string()).collect()
    }
}

fn main() {}
