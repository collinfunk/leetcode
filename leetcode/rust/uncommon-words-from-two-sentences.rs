// Leetcode problem 884: Uncommon Words from Two Sentences.

use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn uncommon_from_sentences(s1: String, s2: String) -> Vec<String> {
        let words1 = s1.split(' ');
        let words2 = s2.split(' ');
        let mut counts1 = HashMap::new();
        let mut counts2 = HashMap::new();
        let mut result: Vec<String> = vec![];
        for word in words1 {
            *counts1.entry(word).or_insert(0) += 1;
        }
        for word in words2 {
            *counts2.entry(word).or_insert(0) += 1;
        }
        for (word, count) in counts1.iter() {
            if *count == 1 && counts2.get(word).is_none() {
                result.push(word.to_string());
            }
        }
        for (word, count) in counts2.iter() {
            if *count == 1 && counts1.get(word).is_none() {
                result.push(word.to_string());
            }
        }
        result
    }
}

fn main() {}
