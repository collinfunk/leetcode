// Leetcode problem 2559: Count Vowel Strings in Ranges.

use std::collections::HashSet;

struct Solution {}

impl Solution {
    pub fn vowel_strings(words: Vec<String>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let vowels = HashSet::from([b'a', b'e', b'i', b'o', b'u']);
        let mut prefix_sum = vec![0; words.len() + 1];
        for i in 0..words.len() {
            let word = words[i].as_bytes();
            if vowels.contains(word.first().unwrap()) && vowels.contains(word.last().unwrap()) {
                prefix_sum[i + 1] = prefix_sum[i] + 1;
            } else {
                prefix_sum[i + 1] = prefix_sum[i];
            }
        }
        let mut result = vec![];
        for query in queries {
            result.push(prefix_sum[query[1] as usize + 1] - prefix_sum[query[0] as usize]);
        }
        result
    }
}

fn main() {}
